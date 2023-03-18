The `proto` directory contains all proto files

The `service` directory contains all service folders

<br>

Push all files to microservices:

```bash
python lavamana.py pull
```

Push all files to microservices except `user`

```bash
python lavamana.py pull --i user

# Or multiple microservices (user and authentication)
python lavamana.py pull --i user+authentication
```
