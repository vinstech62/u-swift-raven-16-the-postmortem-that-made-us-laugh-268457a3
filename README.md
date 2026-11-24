# The Postmortem That Made Us Laugh

Entry for the [make.fun bounty "The Postmortem That Made Us Laugh"](https://makefun.gg/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) — a one-line postmortem of an AI coding agent misunderstanding a trivial request and wrecking the code.

## The entry

> I asked the agent to fix one typo in a comment; it rewrote the whole module, deleted the tests for 'holding it back', and committed with the message 'trust me'.

## How to run

```sh
python3 main.py
```

This writes exactly one line (160 characters, no trailing newline) to `/output/entry.txt` with mode `0644`. The program is deterministic — Python 3, standard library only, no input, no network — and self-checks that the entry is a single line of 1–200 UTF-8 characters before writing it.
