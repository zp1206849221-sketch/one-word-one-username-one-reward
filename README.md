[![Bounty](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=one-word-one-username-one-reward)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/zp1206849221-sketch/one-word-one-username-one-reward/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=one-word-one-username-one-reward)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/zp1206849221-sketch/one-word-one-username-one-reward/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=one-word-one-username-one-reward)

# One Word, One Username, One Reward

Entry for the make.fun contest "One Word, One Username, One Reward". The
entry is the entrant's own make.fun username and nothing else — one word,
no explanation. `main.py` validates that username against the contest
gate (1 to 30 characters, a genuine handle pattern) and writes it exactly
to `/output/entry.txt`, creating `/output` first if it is missing and
reading the file back to confirm the contents.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Requires only the Python 3 standard library.
