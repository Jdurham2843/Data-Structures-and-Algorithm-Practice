CC = g++
CFLAGS = -g -Wall

default: sels

sels: main.o
	$(CC) $(CFLAGS) -o selsort main.o

main.o:
	$(CC) $(CFLAGS) -c main.cc

clean:
	$(RM) selsort *.o *-
