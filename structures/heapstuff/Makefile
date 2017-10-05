CC = g++
CFLAGS = -g -Wall

default: heapprog

heapprog: heap.o main.o
	$(CC) $(CFLAGS) -o program heap.o main.o

heap.o:
	$(CC) $(CFLAGS) -c heap.cpp

main.o:
	$(CC) $(CFLAGS) -c main.cpp

clean:
	$(RM) heapprog *.o *-
