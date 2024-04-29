# ToolsGroup Todo App



#### Docker Build Script (/backend)

```bash
cd /backend
./build_docker.sh
```



## Frontend

#### Development

```bash
npm run dev
```

#### Build

```bash
npm run build
```
*Note: Vue app already build and server with static server see **backend/public***


### 



## Backend

#### Development Server (standalone)

```bash
python3 manage.py run
```
*Note : Fullstack app already build and served by UWSGI python server and docker see **backend/build_docker.sh*** 






## Database

#### Migrate

```bash
python3 manage.py create_db
```

