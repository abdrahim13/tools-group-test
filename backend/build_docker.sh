
IMAGE_NAME="toolsgroup-todo"
CONTAINER_NAME="backend-tools-group-todo"
PORT=5000

# Migrate the database (Simple for sqlite)
function migrate_sqllite_db(){
    echo "💾 Migrating the database..."
    docker exec -it $CONTAINER_NAME python manger.py create_db
    if [ $? -ne 0 ]; then
        echo "❌ Database migration failed"
        exit 1
    fi
    echo "✅ Database migrated successfully"
}

# Remove the container if it exists
if [ $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
    echo "Container ($CONTAINER_NAME)  exists , removing it..."
    docker rm -f $CONTAINER_NAME
    echo "✅ Container removed successfully"
fi

echo "Building docker image..."
docker build -t $IMAGE_NAME .
echo "Running docker container..."
docker run -d --name  $CONTAINER_NAME  -p $PORT:$PORT $IMAGE_NAME 
# Check if container is running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    echo "✅ Docker container is running"
    echo "🚀 Application is running on http://localhost:$PORT"
    migrate_sqllite_db
else
    echo "❌ Docker container is not running"
fi


