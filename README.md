# Exposure Monitor

Review asset-inventory notes for exposure markers.

## Usage
```bash
python exposure_monitor.py sample.txt
python exposure_monitor.py sample.txt --output report.json
```

Python 3.10+; standard library only. Reads only a local UTF-8 text file. No network access, scraping, or source-file modification.

## Detection rules
- `admin`: high heuristic
- `service`: medium heuristic
- `secret`: critical heuristic

Results are heuristic and require human validation. Use only public information or data you are authorized to review. Avoid committing personal or confidential data.

## Tests
`python -m unittest discover -s tests -v`
