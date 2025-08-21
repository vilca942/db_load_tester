This python app is a fastapi backend intended to benchmark different postgresql databases : GCP CloudSql Enterprise, GCP CloudSql Enterprise Plus, GCP AlloyDB etc.

The app enables a simple load test to monitor performances of the different databases (CPU, memory, transactions/sec etc.).

The app comes with some integration tests and a quick CI github pipeline.

The app is run through a docker conteneur and can be deployed on a serverless service like GCP Cloud Run or a kubernetes cluster.

The /write route writes a random string of n characters in the database.

The /count_all route reads all lines and returns the database count.

Other routes can be updated if needed.

Load test is run with k6.
