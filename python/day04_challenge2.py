from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, NamedTuple
from util import read_input
from arpeggio import OneOrMore, ParserPython, EOF
from arpeggio import RegExMatch as _

DAY = 4


class GuardAction(Enum):
    START = auto()
    SLEEP = auto()
    AWAKE = auto()


class GuardRecord(NamedTuple):
    guard_id: int
    timestamp: datetime
    action: GuardAction


def parse_record(line: str) -> List[GuardRecord]:
    def date(): return _(r"\d{4}-\d{2}-\d{2}")
    def time(): return _(r"\d{2}:\d{2}")
    def timestamp(): return date, time
    def guard_ident(): return _(r"\d{1,4}")
    def begin_shift(): return "Guard #", guard_ident, "begins shift"
    def action(): return OneOrMore(["falls asleep", "wakes up", begin_shift])
    def record(): return "[", timestamp, "] ", action, EOF

    tree = (ParserPython(record)).parse(line)
    tstamp = datetime.strptime(f"{tree[1].date.value} {tree[1].time.value}", "%Y-%m-%d %H:%M")

    if tree[3][0].rule_name:
        guard_id = tree[3][0][1].value
        return GuardRecord(guard_id, tstamp, GuardAction.START)
    if 'asleep' in tree[3][0].value:
        return GuardRecord(None, tstamp, GuardAction.SLEEP)
    if 'wakes' in tree[3][0].value:
        return GuardRecord(None, tstamp, GuardAction.AWAKE)


def resolve_guard_ids(records: List[GuardRecord]) -> List[GuardRecord]:
    records.sort(key=lambda x: x.timestamp)
    last_id = None
    for idx, record in enumerate(records):
        if record.guard_id:
            last_id = record.guard_id
            continue
        records[idx] = GuardRecord(last_id, record.timestamp, record.action)
    return records


# Dictionary of minutes a guard slept, and how many times it happened
def minutes_slept(records: List[GuardRecord]) -> Dict[int, int]:
    guard_id: int = records[0].guard_id
    minute_map: Dict[int, int] = {}
    sleep_minute: int = None

    for record in records:
        if record.guard_id != guard_id:
            raise ValueError("Mutiple Guard ID's Provided.")
        if record.action == GuardAction.SLEEP:
            sleep_minute = record.timestamp.minute
        elif record.action == GuardAction.AWAKE:
            awake_minute = record.timestamp.minute
            for idx in range(sleep_minute, awake_minute):
                if idx in minute_map.keys():
                    minute_map[idx] += 1
                else:
                    minute_map[idx] = 1
    return minute_map


def main():
    lines = read_input(DAY)
    records = [parse_record(line) for line in lines]
    records = resolve_guard_ids(records)
    guard_ids = set([record.guard_id for record in records])

    max_occurances: int = 0
    max_minute: int = None
    max_guard_id: int = None

    for guard_id in guard_ids:
        guard_records = [record for record in records if record.guard_id == guard_id]
        guard_minutes = minutes_slept(guard_records)
        if len(guard_minutes) == 0:
            continue
        max_count = max(guard_minutes.values())

        if max_count > max_occurances:
            max_guard_id = int(guard_id)
            max_occurances = max_count
            max_minute = [k for k, v in guard_minutes.items() if v == max_count][0]

    print(max_guard_id * max_minute)


if __name__ == "__main__":
    main()
