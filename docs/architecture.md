# Architecture

RepoLens scans files, calculates metrics, diagnoses repository issues, computes a
health score, and sends the resulting report to one or more output formatters.

The analysis layer does not modify the inspected repository.
