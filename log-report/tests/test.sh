#!/bin/bash
# pytest deps are baked into the image; run and record the reward.
mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
rc=$?

if [ "$rc" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit "$rc"
