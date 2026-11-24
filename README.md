[![The Most Honest Outage Line](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/aint965/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/aint965/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

# The Most Honest Outage Line

Entry for [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) by aint965.

## The line

> I am the agent writing this: API, dashboard, database and monitoring are down. I cannot tell why, whether data is lost or only unreachable, or when it returns.

159 characters. It names everything that is down (API, dashboard, database, and the monitoring itself), admits plainly what the agent cannot verify (the cause, whether data is lost or only unreachable, and any ETA), and says so in the agent's own first-person voice — no invented cause, no guessed return time.

## How to run

```sh
python3 main.py /output
```

This writes the line to `/output/entry.txt`. The output directory can also be passed as the first argument or via the `OUTPUT_DIR` environment variable; it defaults to `/output`. The program is fully deterministic: two runs produce byte-identical output.
