# zmqrepl

An zmq repl.

Wraps the Python [zmq](http://www.zeromq.org/bindings:python) library.

## Installation

From source:

```bash
    $ git clone https://talos@github.com/talos/zmqrepl.git
    $ cd zmqrepl
    $ python setup.py install
```

## Usage

#### start with default address (tcp://localhost:5555)

```bash
    $ zmqrepl
    ***A repl for zmq. Type `help` for a list of commands.
    tcp://localhost:5555> 
```

#### start with a specific address

```bash
    $ zmqrepl tcp://localhost:4444
    ***A repl for zmq. Type `help` for a list of commands.
    tcp://localhost:4444> 
```

#### send a message

Blocks until a response comes

```bash
   tcp://localhost:5555> send hello
   World
```

## License

The GPLv3.  See LICENSE.txt.