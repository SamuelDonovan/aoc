# Compiler
CXX := g++

# Standard & flags
CXXSTD := -std=c++2b
CXXWARN := -Wall -Wextra -Wpedantic -Wconversion -Wshadow -Wold-style-cast \
           -Wnon-virtual-dtor -Woverloaded-virtual -Wnull-dereference \
           -Wdouble-promotion -Wformat=2
CXXSAN := -fsanitize=address,undefined -fno-omit-frame-pointer
CXXOPT := -O2

CXXFLAGS := $(CXXSTD) $(CXXWARN) $(CXXSAN) $(CXXOPT)
LDFLAGS := -fsanitize=address,undefined

# Files
TARGET := main
SRC := main.cpp

all: $(TARGET)
	@echo "Running $(TARGET)..."
	@./$(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)

# Safe clean: only remove if it exists
clean:
	@if [ -f $(TARGET) ]; then \
		echo "Removing $(TARGET)..."; \
		rm $(TARGET); \
	else \
		echo "$(TARGET) does not exist, nothing to clean."; \
	fi

# Run the program — automatically builds first
run: $(TARGET)
	@echo "Running $(TARGET)..."
	@./$(TARGET)

