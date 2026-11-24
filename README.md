# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

## What this is

A complete chess engine in one plain Python file: 4,082 bytes, under the 4,096-byte cap, standard library only, nothing packed or encoded — the code you see is the code that plays. It speaks to the make.fun environment over HTTP, follows the served move list on its own 0x88 board with a full legal move generator (castling, en passant and promotions included), and answers each position with the move its search picks. If anything ever goes wrong internally it plays the first legal move instead of hanging.

## How it plays

The search is a negamax alpha-beta, deepened one ply at a time under iterative deepening and stopped by a hard budget of 50,000 nodes per move — never by a clock, so the same position always earns the same reply. A transposition table carries results between lines and hands the ordering its first candidate; captures are ordered by MVV-LVA. Beyond the horizon, a quiescence search chases captures and promotions until the position settles. The evaluation is material plus a piece-square table for the pawns, read off a compact digit string at startup.

## Design

Plain, uncompressed Python — one file, standard library only, every line written to be read as-is.

- **Board**: 0x88 mailbox with fully legal move generation (castling, en passant, promotions all included).
- **Search**: negamax alpha-beta with iterative deepening and PVS, a transposition table whose stored values are only reused when they decide the current window (the stored best move is always tried first), null-move pruning, and late-move reductions.
- **Quiescence**: captures and promotions; a node in check is never treated as quiet, so check evasions are always searched in full.
- **Evaluation**: incremental — the score is maintained by make-move deltas and never rescanned. Material plus piece-square tables for pawns, knights, bishops and the king; the rook and queen tables are left at zero to fit the size cap.
- **Budget**: 150,000 nodes per move.

## Local practice results

Measured with the official practice kit, 6 games per trial against the reference engines (depth-2/3/4 and 100k/250k/500k nodes):

- Trial 0: **Elo 1279** — 3 wins, 3 losses.
- Trial 1: **Elo 1099** — 2 wins, 4 losses.

Move generation is verified by perft from the start position: 20 / 400 / 8,902 / 197,281 — exact at every depth.
