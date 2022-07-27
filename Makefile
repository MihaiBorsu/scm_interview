


all: build
	$(info Done.)

greeting:
	$(info Building super important repo)


build: greeting
	g++ helloworld/HelloWorld.cpp -o helloworld.o

clean:
	rm helloworld.o
	rm -rf ./tmp
