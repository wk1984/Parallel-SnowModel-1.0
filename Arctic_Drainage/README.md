# USING Docker ...

   cd ~/Documents/GitHub/Parallel-SnowModel-1.0/example

   docker run -it --name test2 --volume=$PWD:/home:delegated --workdir=/home -p 3210:8888 --restart=no --runtime=runc -t -d wk1984/parallel_snowmodel:v1.0

