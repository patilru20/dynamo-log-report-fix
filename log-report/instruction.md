An Apache-style access log is at /app/access.log. Summarize it and write the result to /app/report.json.

The report must be a single JSON object with exactly three keys:

- "total_requests": integer, the number of non-blank lines in the log.
- "unique_ips": integer, the number of distinct client IPs (the first whitespace-separated field on each line).
- "top_path": string, the most requested path, taken from the quoted request line (e.g. "/index.html" from "GET /index.html HTTP/1.1").

Success criteria:

1. /app/report.json exists and is a single valid JSON object.
2. It has only the keys "total_requests", "unique_ips", and "top_path".
3. "total_requests" is the number of non-blank lines in the log.
4. "unique_ips" is the number of distinct client IPs in the log.
5. "top_path" is the most frequently requested path in the log.
