# Social Network

Console-based social network application.

## Setup

```
pip install -r requirements.txt
```

## Run

```
python main.py
```

## Tests

```
pytest
```

## Usage

Commands:

- **Post**: `Alice -> I love the weather today`
- **Read**: `Alice` (shows their timeline)
- **Follow**: `Charlie follows Alice`
- **Wall**: `Charlie wall` (shows aggregated timeline)

## Approach

I built this incrementally, starting from the core domain (posting and reading) and layering features on top one at a time. Each step has its own commit so you can see the progression.

The main design choice was to keep the business logic (`SocialNetwork`) completely separate from input parsing (`CommandParser`) and display formatting (`TimeFormatter`). This way each piece can be tested in isolation and swapped out if needed.

I introduced a `Clock` abstraction so that tests can control time deterministically instead of relying on `datetime.now()`, which would make time-related assertions flaky.

## Assumptions

- Usernames are single words (no spaces).
- Users don't need to be explicitly registered before posting or following.
- All data lives in memory for the duration of the session. No persistence between runs.
- The `->` separator in post commands is unique enough that it won't conflict with normal message content.

## Trade-offs

- I used `namedtuple` for commands instead of a full class hierarchy. This keeps things simple but means adding complex command behavior (like validation or undo) would require a refactor.
- Data structures are plain dicts and lists. Fine for this scale, but would need indexing or a proper database for larger datasets.
- The prompt `> ` is written to the same output stream as results, which made integration testing a bit trickier. In a real app I might separate those concerns.
