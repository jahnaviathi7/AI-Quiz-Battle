import json
import os
import random
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------
# ENVIRONMENT
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()


# ---------------------------------------------------------
# CATEGORY-SPECIFIC QUESTION BANK
# ---------------------------------------------------------

QUESTION_BANK = {

    # =====================================================
    # PYTHON
    # =====================================================
    "Python": {
        "Easy": [
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "correct_answer": "def"
            },
            {
                "question": "Which data type stores key-value pairs in Python?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "correct_answer": "Dictionary"
            },
            {
                "question": "Which symbol is used for a single-line comment in Python?",
                "options": ["//", "#", "/*", "--"],
                "correct_answer": "#"
            },
            {
                "question": "Which function is used to find the length of a Python object?",
                "options": ["size()", "length()", "len()", "count()"],
                "correct_answer": "len()"
            },
            {
                "question": "Which of these is a mutable Python data structure?",
                "options": ["Tuple", "String", "List", "Integer"],
                "correct_answer": "List"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["object", "class", "struct", "new"],
                "correct_answer": "class"
            },
            {
                "question": "Which operator is used for exponentiation in Python?",
                "options": ["^", "**", "//", "%%"],
                "correct_answer": "**"
            },
            {
                "question": "Which function displays output in Python?",
                "options": ["display()", "echo()", "print()", "output()"],
                "correct_answer": "print()"
            },
        ],

        "Medium": [
            {
                "question": "What does a Python list comprehension provide?",
                "options": [
                    "A way to create lists using a compact syntax",
                    "A way to create classes",
                    "A database connection",
                    "A method for exception handling"
                ],
                "correct_answer": "A way to create lists using a compact syntax"
            },
            {
                "question": "What is the main purpose of the __init__ method in a Python class?",
                "options": [
                    "Destroy an object",
                    "Initialize an object",
                    "Import a module",
                    "Handle exceptions"
                ],
                "correct_answer": "Initialize an object"
            },
            {
                "question": "Which keyword is used to handle exceptions in Python?",
                "options": ["catch", "try", "error", "handle"],
                "correct_answer": "try"
            },
            {
                "question": "What does the map() function generally return in Python 3?",
                "options": [
                    "A list",
                    "A map iterator",
                    "A dictionary",
                    "A tuple"
                ],
                "correct_answer": "A map iterator"
            },
            {
                "question": "Which Python feature allows a function to remember variables from its enclosing scope?",
                "options": ["Inheritance", "Closure", "Overloading", "Casting"],
                "correct_answer": "Closure"
            },
            {
                "question": "What is the purpose of the self parameter in a Python instance method?",
                "options": [
                    "It refers to the current object",
                    "It creates a new class",
                    "It imports a module",
                    "It handles errors"
                ],
                "correct_answer": "It refers to the current object"
            },
            {
                "question": "Which module is commonly used to work with JSON in Python?",
                "options": ["json", "data", "picklejson", "js"],
                "correct_answer": "json"
            },
            {
                "question": "What does the with statement commonly help manage?",
                "options": [
                    "Resources such as files",
                    "Only loops",
                    "Only functions",
                    "Variables only"
                ],
                "correct_answer": "Resources such as files"
            },
        ],

        "Hard": [
            {
                "question": "What is the primary purpose of a Python decorator?",
                "options": [
                    "Modify or extend function behavior",
                    "Create database tables",
                    "Compile Python code",
                    "Delete objects"
                ],
                "correct_answer": "Modify or extend function behavior"
            },
            {
                "question": "What does the Global Interpreter Lock (GIL) primarily affect in CPython?",
                "options": [
                    "Execution of Python bytecode by multiple threads",
                    "Database queries",
                    "File permissions",
                    "Network routing"
                ],
                "correct_answer": "Execution of Python bytecode by multiple threads"
            },
            {
                "question": "What is a generator in Python?",
                "options": [
                    "An object that yields values lazily",
                    "A compiler",
                    "A database engine",
                    "A GUI framework"
                ],
                "correct_answer": "An object that yields values lazily"
            },
            {
                "question": "Which method is called by the iter() function to obtain an iterator?",
                "options": ["__next__", "__iter__", "__iterator__", "__loop__"],
                "correct_answer": "__iter__"
            },
            {
                "question": "Which special method is used to retrieve the next item from an iterator?",
                "options": ["__next__", "__iter__", "__get__", "__item__"],
                "correct_answer": "__next__"
            },
            {
                "question": "What is method resolution order (MRO) used for in Python?",
                "options": [
                    "Determining the order in which base classes are searched",
                    "Sorting dictionary keys",
                    "Ordering imports",
                    "Sorting function arguments"
                ],
                "correct_answer": "Determining the order in which base classes are searched"
            },
        ],
    },

    # =====================================================
    # JAVA
    # =====================================================
    "Java": {
        "Easy": [
            {
                "question": "Which keyword is used to create a class in Java?",
                "options": ["class", "struct", "define", "object"],
                "correct_answer": "class"
            },
            {
                "question": "Which method is the entry point of a Java application?",
                "options": ["start()", "run()", "main()", "execute()"],
                "correct_answer": "main()"
            },
            {
                "question": "Which keyword is used for inheritance in Java?",
                "options": ["inherits", "extends", "implements", "super"],
                "correct_answer": "extends"
            },
            {
                "question": "Which Java type stores true or false values?",
                "options": ["boolean", "bool", "bit", "logical"],
                "correct_answer": "boolean"
            },
            {
                "question": "Which component executes Java bytecode?",
                "options": ["JVM", "JDK", "JAR", "Javadoc"],
                "correct_answer": "JVM"
            },
            {
                "question": "Which keyword creates an object in Java?",
                "options": ["create", "object", "new", "make"],
                "correct_answer": "new"
            },
        ],

        "Medium": [
            {
                "question": "What is method overloading in Java?",
                "options": [
                    "Same method name with different parameter lists",
                    "Replacing a class",
                    "Deleting a method",
                    "Creating multiple packages"
                ],
                "correct_answer": "Same method name with different parameter lists"
            },
            {
                "question": "Which keyword is used to implement an interface?",
                "options": ["extends", "interface", "implements", "inherits"],
                "correct_answer": "implements"
            },
            {
                "question": "Which collection does not allow duplicate elements?",
                "options": ["List", "Set", "ArrayList", "Vector"],
                "correct_answer": "Set"
            },
            {
                "question": "What is encapsulation in Java?",
                "options": [
                    "Bundling data and methods together",
                    "Creating multiple JVMs",
                    "Running multiple programs",
                    "Compiling code twice"
                ],
                "correct_answer": "Bundling data and methods together"
            },
            {
                "question": "Which keyword prevents a class from being inherited?",
                "options": ["static", "final", "private", "sealed"],
                "correct_answer": "final"
            },
            {
                "question": "Which exception occurs when an integer is divided by zero?",
                "options": [
                    "NullPointerException",
                    "ArithmeticException",
                    "IOException",
                    "ClassNotFoundException"
                ],
                "correct_answer": "ArithmeticException"
            },
        ],

        "Hard": [
            {
                "question": "What is the main difference between HashMap and TreeMap?",
                "options": [
                    "TreeMap maintains sorted keys while HashMap does not guarantee sorting",
                    "HashMap stores only strings",
                    "TreeMap cannot store objects",
                    "There is no difference"
                ],
                "correct_answer": "TreeMap maintains sorted keys while HashMap does not guarantee sorting"
            },
            {
                "question": "What does the volatile keyword provide in Java?",
                "options": [
                    "Visibility of changes across threads",
                    "Object serialization",
                    "Memory allocation",
                    "Method overloading"
                ],
                "correct_answer": "Visibility of changes across threads"
            },
            {
                "question": "Which mechanism automatically reclaims unused objects in Java?",
                "options": [
                    "Destructor",
                    "Garbage collection",
                    "Pointer arithmetic",
                    "Memory compiler"
                ],
                "correct_answer": "Garbage collection"
            },
            {
                "question": "What is a functional interface in Java?",
                "options": [
                    "An interface with exactly one abstract method",
                    "An interface with no methods",
                    "A class with one constructor",
                    "A static interface"
                ],
                "correct_answer": "An interface with exactly one abstract method"
            },
        ],
    },

    # =====================================================
    # C PROGRAMMING
    # =====================================================
    "C Programming": {
        "Easy": [
            {
                "question": "Which function is the starting point of a C program?",
                "options": ["start()", "main()", "begin()", "run()"],
                "correct_answer": "main()"
            },
            {
                "question": "Which symbol ends a C statement?",
                "options": [".", ":", ";", ","],
                "correct_answer": ";"
            },
            {
                "question": "Which header file is commonly used for printf()?",
                "options": ["stdlib.h", "stdio.h", "string.h", "math.h"],
                "correct_answer": "stdio.h"
            },
            {
                "question": "Which data type stores a single character?",
                "options": ["char", "character", "string", "byte"],
                "correct_answer": "char"
            },
            {
                "question": "Which operator is used to get the address of a variable?",
                "options": ["*", "&", "@", "#"],
                "correct_answer": "&"
            },
            {
                "question": "Which loop executes its body at least once?",
                "options": ["for", "while", "do-while", "foreach"],
                "correct_answer": "do-while"
            },
        ],

        "Medium": [
            {
                "question": "What is a pointer in C?",
                "options": [
                    "A variable that stores an address",
                    "A variable that stores only strings",
                    "A loop",
                    "A function"
                ],
                "correct_answer": "A variable that stores an address"
            },
            {
                "question": "Which function dynamically allocates memory in C?",
                "options": ["alloc()", "malloc()", "new()", "create()"],
                "correct_answer": "malloc()"
            },
            {
                "question": "Which function releases dynamically allocated memory?",
                "options": ["remove()", "clear()", "free()", "delete()"],
                "correct_answer": "free()"
            },
            {
                "question": "What is a structure in C?",
                "options": [
                    "A user-defined type that groups related variables",
                    "A loop",
                    "A compiler",
                    "A pointer operator"
                ],
                "correct_answer": "A user-defined type that groups related variables"
            },
            {
                "question": "Which function compares two strings in C?",
                "options": ["strcmp()", "compare()", "strcompare()", "equals()"],
                "correct_answer": "strcmp()"
            },
        ],

        "Hard": [
            {
                "question": "What is a dangling pointer?",
                "options": [
                    "A pointer referring to memory that is no longer valid",
                    "A pointer with value zero",
                    "A pointer to a function",
                    "A pointer to a constant"
                ],
                "correct_answer": "A pointer referring to memory that is no longer valid"
            },
            {
                "question": "What does pointer arithmetic depend on?",
                "options": [
                    "Size of the pointed-to data type",
                    "CPU temperature",
                    "Variable name",
                    "Compiler version only"
                ],
                "correct_answer": "Size of the pointed-to data type"
            },
            {
                "question": "What is a function pointer in C?",
                "options": [
                    "A pointer that stores the address of a function",
                    "A function returning a pointer only",
                    "A pointer to an integer",
                    "A special loop"
                ],
                "correct_answer": "A pointer that stores the address of a function"
            },
        ],
    },

    # =====================================================
    # C++
    # =====================================================
    "C++": {
        "Easy": [
            {
                "question": "Which feature allows C++ to support object-oriented programming?",
                "options": ["Classes", "Only arrays", "Preprocessors", "Macros"],
                "correct_answer": "Classes"
            },
            {
                "question": "Which keyword creates an object dynamically in C++?",
                "options": ["malloc", "new", "create", "object"],
                "correct_answer": "new"
            },
            {
                "question": "Which symbol is used for scope resolution?",
                "options": [".", "::", "->", "#"],
                "correct_answer": "::"
            },
            {
                "question": "Which container stores elements in a dynamic array?",
                "options": ["vector", "stack", "map", "set"],
                "correct_answer": "vector"
            },
        ],

        "Medium": [
            {
                "question": "What is function overloading?",
                "options": [
                    "Multiple functions with the same name but different parameters",
                    "Deleting functions",
                    "Calling a function twice",
                    "Creating virtual functions"
                ],
                "correct_answer": "Multiple functions with the same name but different parameters"
            },
            {
                "question": "Which keyword declares a virtual function?",
                "options": ["virtual", "dynamic", "override", "abstract"],
                "correct_answer": "virtual"
            },
            {
                "question": "Which STL container stores key-value pairs?",
                "options": ["vector", "map", "stack", "queue"],
                "correct_answer": "map"
            },
            {
                "question": "What is encapsulation?",
                "options": [
                    "Combining data and methods within a class",
                    "Creating pointers",
                    "Using multiple files",
                    "Compiling templates"
                ],
                "correct_answer": "Combining data and methods within a class"
            },
        ],

        "Hard": [
            {
                "question": "What is the purpose of a virtual destructor?",
                "options": [
                    "To ensure proper destruction through a base-class pointer",
                    "To prevent object creation",
                    "To create templates",
                    "To overload operators"
                ],
                "correct_answer": "To ensure proper destruction through a base-class pointer"
            },
            {
                "question": "What is RAII in C++?",
                "options": [
                    "Resource Acquisition Is Initialization",
                    "Runtime Array Access Interface",
                    "Random Access Initialization",
                    "Resource Allocation And Inheritance"
                ],
                "correct_answer": "Resource Acquisition Is Initialization"
            },
            {
                "question": "What does std::move primarily enable?",
                "options": [
                    "Move semantics",
                    "Garbage collection",
                    "Thread creation",
                    "Exception handling"
                ],
                "correct_answer": "Move semantics"
            },
        ],
    },

    # =====================================================
    # JAVASCRIPT
    # =====================================================
    "JavaScript": {
        "Easy": [
            {
                "question": "Which keyword declares a block-scoped variable that can be reassigned?",
                "options": ["var", "let", "const", "define"],
                "correct_answer": "let"
            },
            {
                "question": "Which symbol is commonly used for strict equality?",
                "options": ["=", "==", "===", "!="],
                "correct_answer": "==="
            },
            {
                "question": "Which method adds an element to the end of an array?",
                "options": ["push()", "add()", "append()", "insert()"],
                "correct_answer": "push()"
            },
            {
                "question": "Which keyword declares a constant?",
                "options": ["constant", "let", "const", "static"],
                "correct_answer": "const"
            },
        ],

        "Medium": [
            {
                "question": "What is a closure in JavaScript?",
                "options": [
                    "A function retaining access to its lexical scope",
                    "A closed browser tab",
                    "A loop",
                    "A class constructor"
                ],
                "correct_answer": "A function retaining access to its lexical scope"
            },
            {
                "question": "What does Promise represent in JavaScript?",
                "options": [
                    "An eventual result of an asynchronous operation",
                    "A CSS rule",
                    "A database table",
                    "A synchronous loop"
                ],
                "correct_answer": "An eventual result of an asynchronous operation"
            },
            {
                "question": "Which method creates a new array by transforming each element?",
                "options": ["filter()", "map()", "reduce()", "find()"],
                "correct_answer": "map()"
            },
            {
                "question": "What does JSON.parse() do?",
                "options": [
                    "Converts JSON text into a JavaScript value",
                    "Converts JavaScript to HTML",
                    "Creates a Promise",
                    "Encrypts data"
                ],
                "correct_answer": "Converts JSON text into a JavaScript value"
            },
        ],

        "Hard": [
            {
                "question": "What is the event loop responsible for?",
                "options": [
                    "Coordinating asynchronous callbacks and the call stack",
                    "Rendering CSS only",
                    "Creating HTML elements",
                    "Compiling Java"
                ],
                "correct_answer": "Coordinating asynchronous callbacks and the call stack"
            },
            {
                "question": "What is hoisting in JavaScript?",
                "options": [
                    "The processing of certain declarations before code execution",
                    "Moving HTML elements upward",
                    "Increasing CPU priority",
                    "Encrypting variables"
                ],
                "correct_answer": "The processing of certain declarations before code execution"
            },
            {
                "question": "What does async/await simplify?",
                "options": [
                    "Working with Promises",
                    "CSS animations",
                    "DOM styling",
                    "Array sorting only"
                ],
                "correct_answer": "Working with Promises"
            },
        ],
    },

    # =====================================================
    # REACT
    # =====================================================
    "React": {
        "Easy": [
            {
                "question": "What is React primarily used for?",
                "options": [
                    "Building user interfaces",
                    "Managing databases",
                    "Operating systems",
                    "Network routing"
                ],
                "correct_answer": "Building user interfaces"
            },
            {
                "question": "What is JSX?",
                "options": [
                    "A syntax extension for JavaScript",
                    "A database language",
                    "A CSS framework",
                    "A Python library"
                ],
                "correct_answer": "A syntax extension for JavaScript"
            },
            {
                "question": "Which hook is used to manage state in a functional component?",
                "options": ["useState", "useData", "useValue", "useComponent"],
                "correct_answer": "useState"
            },
            {
                "question": "What is a React component?",
                "options": [
                    "A reusable UI building block",
                    "A database table",
                    "A server",
                    "A CSS file"
                ],
                "correct_answer": "A reusable UI building block"
            },
        ],

        "Medium": [
            {
                "question": "What is the purpose of useEffect?",
                "options": [
                    "Perform side effects in a component",
                    "Create CSS classes",
                    "Create database tables",
                    "Compile JavaScript"
                ],
                "correct_answer": "Perform side effects in a component"
            },
            {
                "question": "What are props in React?",
                "options": [
                    "Data passed from a parent component to a child",
                    "Global CSS variables",
                    "Database records",
                    "Browser plugins"
                ],
                "correct_answer": "Data passed from a parent component to a child"
            },
            {
                "question": "Why is a key prop used when rendering lists?",
                "options": [
                    "To help React identify elements efficiently",
                    "To encrypt elements",
                    "To style elements",
                    "To create APIs"
                ],
                "correct_answer": "To help React identify elements efficiently"
            },
            {
                "question": "What is conditional rendering?",
                "options": [
                    "Rendering UI based on a condition",
                    "Changing CSS only",
                    "Creating multiple servers",
                    "Deleting components"
                ],
                "correct_answer": "Rendering UI based on a condition"
            },
        ],

        "Hard": [
            {
                "question": "What problem does React reconciliation address?",
                "options": [
                    "Determining efficient DOM updates",
                    "Database indexing",
                    "HTTP encryption",
                    "File compression"
                ],
                "correct_answer": "Determining efficient DOM updates"
            },
            {
                "question": "What is a controlled component in React?",
                "options": [
                    "A form element whose value is controlled by React state",
                    "A component controlled by CSS",
                    "A server component only",
                    "A component without state"
                ],
                "correct_answer": "A form element whose value is controlled by React state"
            },
            {
                "question": "Why should state updates generally be treated as immutable?",
                "options": [
                    "To allow React to correctly detect state changes",
                    "To improve CSS",
                    "To create database indexes",
                    "To prevent JavaScript execution"
                ],
                "correct_answer": "To allow React to correctly detect state changes"
            },
        ],
    },

    # =====================================================
    # HTML & CSS
    # =====================================================
    "HTML & CSS": {
        "Easy": [
            {
                "question": "What does HTML stand for?",
                "options": [
                    "HyperText Markup Language",
                    "HighText Machine Language",
                    "Hyperlink Text Management Language",
                    "Home Tool Markup Language"
                ],
                "correct_answer": "HyperText Markup Language"
            },
            {
                "question": "Which HTML tag creates a hyperlink?",
                "options": ["<link>", "<a>", "<href>", "<url>"],
                "correct_answer": "<a>"
            },
            {
                "question": "Which CSS property changes text color?",
                "options": ["font-color", "color", "text-color", "foreground"],
                "correct_answer": "color"
            },
            {
                "question": "Which HTML tag creates the largest heading?",
                "options": ["<h6>", "<head>", "<h1>", "<heading>"],
                "correct_answer": "<h1>"
            },
        ],

        "Medium": [
            {
                "question": "What is the CSS box model?",
                "options": [
                    "Content, padding, border, and margin",
                    "Header, body, footer",
                    "HTML, CSS, JavaScript",
                    "Grid, flex, table"
                ],
                "correct_answer": "Content, padding, border, and margin"
            },
            {
                "question": "Which CSS layout system is designed for one-dimensional layouts?",
                "options": ["Flexbox", "Grid", "Float", "Table"],
                "correct_answer": "Flexbox"
            },
            {
                "question": "Which HTML element is semantic for navigation links?",
                "options": ["<navigate>", "<nav>", "<links>", "<menu-bar>"],
                "correct_answer": "<nav>"
            },
            {
                "question": "What does CSS specificity determine?",
                "options": [
                    "Which CSS rule takes precedence",
                    "Page loading speed",
                    "HTML validity",
                    "Image resolution"
                ],
                "correct_answer": "Which CSS rule takes precedence"
            },
        ],

        "Hard": [
            {
                "question": "Which CSS layout system is best suited for two-dimensional layouts?",
                "options": ["Flexbox", "Grid", "Inline", "Float"],
                "correct_answer": "Grid"
            },
            {
                "question": "What does position: sticky allow an element to do?",
                "options": [
                    "Remain positioned relative to scrolling within its container",
                    "Always remain fixed to the browser viewport",
                    "Become invisible",
                    "Disable scrolling"
                ],
                "correct_answer": "Remain positioned relative to scrolling within its container"
            },
        ],
    },

    # =====================================================
    # DATA STRUCTURES
    # =====================================================
    "Data Structures": {
        "Easy": [
            {
                "question": "Which data structure follows LIFO?",
                "options": ["Queue", "Stack", "Tree", "Graph"],
                "correct_answer": "Stack"
            },
            {
                "question": "Which data structure follows FIFO?",
                "options": ["Stack", "Queue", "Tree", "Heap"],
                "correct_answer": "Queue"
            },
            {
                "question": "Which data structure consists of nodes connected by links?",
                "options": ["Array", "Linked List", "Stack", "Hash"],
                "correct_answer": "Linked List"
            },
            {
                "question": "Which structure is commonly used for hierarchical data?",
                "options": ["Tree", "Array", "Stack", "Queue"],
                "correct_answer": "Tree"
            },
        ],

        "Medium": [
            {
                "question": "What is the average search complexity of a hash table?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": "O(1)"
            },
            {
                "question": "Which traversal uses a queue in graph algorithms?",
                "options": ["DFS", "BFS", "Inorder", "Postorder"],
                "correct_answer": "BFS"
            },
            {
                "question": "Which traversal is commonly implemented using a stack?",
                "options": ["BFS", "DFS", "Level order", "Counting"],
                "correct_answer": "DFS"
            },
            {
                "question": "What is the root node of a tree?",
                "options": [
                    "The topmost node",
                    "The last node",
                    "A leaf node",
                    "A node with no parent and no children"
                ],
                "correct_answer": "The topmost node"
            },
        ],

        "Hard": [
            {
                "question": "What is the time complexity of searching in a balanced binary search tree?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "correct_answer": "O(log n)"
            },
            {
                "question": "What is the main purpose of a heap?",
                "options": [
                    "Efficient access to the minimum or maximum element",
                    "Store strings only",
                    "Perform graph traversal",
                    "Store duplicate-free values only"
                ],
                "correct_answer": "Efficient access to the minimum or maximum element"
            },
            {
                "question": "Which data structure is commonly used to implement a priority queue?",
                "options": ["Heap", "Stack", "Linked list only", "Graph"],
                "correct_answer": "Heap"
            },
        ],
    },

    # =====================================================
    # ALGORITHMS
    # =====================================================
    "Algorithms": {
        "Easy": [
            {
                "question": "Which algorithm searches an element by repeatedly dividing a sorted array?",
                "options": ["Linear Search", "Binary Search", "DFS", "BFS"],
                "correct_answer": "Binary Search"
            },
            {
                "question": "Which sorting algorithm repeatedly swaps adjacent elements?",
                "options": ["Merge Sort", "Bubble Sort", "Quick Sort", "Heap Sort"],
                "correct_answer": "Bubble Sort"
            },
            {
                "question": "What does algorithm complexity measure?",
                "options": [
                    "Resource usage as input size grows",
                    "Code color",
                    "Variable names",
                    "Screen size"
                ],
                "correct_answer": "Resource usage as input size grows"
            },
        ],

        "Medium": [
            {
                "question": "What is the average time complexity of Quick Sort?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(n²)"],
                "correct_answer": "O(n log n)"
            },
            {
                "question": "Which algorithm uses divide and conquer to sort data?",
                "options": ["Merge Sort", "Bubble Sort", "Linear Search", "BFS"],
                "correct_answer": "Merge Sort"
            },
            {
                "question": "Which technique solves a problem by making locally optimal choices?",
                "options": ["Greedy", "Backtracking", "Brute Force", "Hashing"],
                "correct_answer": "Greedy"
            },
        ],

        "Hard": [
            {
                "question": "What is the time complexity of Dijkstra's algorithm with a binary heap implementation?",
                "options": [
                    "O((V + E) log V)",
                    "O(V²E)",
                    "O(E²)",
                    "O(log V)"
                ],
                "correct_answer": "O((V + E) log V)"
            },
            {
                "question": "Which technique stores solutions to overlapping subproblems?",
                "options": [
                    "Dynamic Programming",
                    "Greedy",
                    "Binary Search",
                    "Randomization"
                ],
                "correct_answer": "Dynamic Programming"
            },
            {
                "question": "Which algorithm finds a minimum spanning tree by repeatedly choosing the smallest safe edge?",
                "options": ["Kruskal's algorithm", "Binary Search", "BFS", "KMP"],
                "correct_answer": "Kruskal's algorithm"
            },
        ],
    },

    # =====================================================
    # DBMS
    # =====================================================
    "DBMS": {
        "Easy": [
            {
                "question": "What does DBMS stand for?",
                "options": [
                    "Database Management System",
                    "Data Backup Management System",
                    "Database Machine System",
                    "Data Business Management Software"
                ],
                "correct_answer": "Database Management System"
            },
            {
                "question": "Which language is commonly used to query relational databases?",
                "options": ["HTML", "SQL", "CSS", "XML"],
                "correct_answer": "SQL"
            },
            {
                "question": "Which key uniquely identifies a row?",
                "options": ["Foreign Key", "Primary Key", "Candidate Key only", "Index"],
                "correct_answer": "Primary Key"
            },
            {
                "question": "What is a table made up of?",
                "options": ["Rows and columns", "Only rows", "Only columns", "Queries"],
                "correct_answer": "Rows and columns"
            },
        ],

        "Medium": [
            {
                "question": "What is normalization used for?",
                "options": [
                    "Reducing data redundancy",
                    "Increasing duplicate data",
                    "Encrypting passwords",
                    "Creating indexes only"
                ],
                "correct_answer": "Reducing data redundancy"
            },
            {
                "question": "What does a foreign key represent?",
                "options": [
                    "A reference to a key in another table",
                    "A password",
                    "A temporary column",
                    "A database server"
                ],
                "correct_answer": "A reference to a key in another table"
            },
            {
                "question": "Which SQL command retrieves data?",
                "options": ["SELECT", "GET", "FETCHROW", "READ"],
                "correct_answer": "SELECT"
            },
            {
                "question": "Which SQL clause filters rows?",
                "options": ["WHERE", "ORDER", "GROUP", "FILTER"],
                "correct_answer": "WHERE"
            },
        ],

        "Hard": [
            {
                "question": "What does ACID stand for in database transactions?",
                "options": [
                    "Atomicity, Consistency, Isolation, Durability",
                    "Access, Control, Index, Data",
                    "Atomicity, Control, Integrity, Data",
                    "Access, Consistency, Isolation, Data"
                ],
                "correct_answer": "Atomicity, Consistency, Isolation, Durability"
            },
            {
                "question": "What is a database index primarily used for?",
                "options": [
                    "Improving query lookup performance",
                    "Encrypting tables",
                    "Deleting duplicates",
                    "Replacing primary keys"
                ],
                "correct_answer": "Improving query lookup performance"
            },
            {
                "question": "What is a deadlock in database systems?",
                "options": [
                    "Transactions waiting indefinitely for resources held by each other",
                    "A deleted table",
                    "A failed SELECT query",
                    "An invalid column"
                ],
                "correct_answer": "Transactions waiting indefinitely for resources held by each other"
            },
        ],
    },

    # =====================================================
    # OPERATING SYSTEMS
    # =====================================================
    "Operating Systems": {
        "Easy": [
            {
                "question": "What is an operating system?",
                "options": [
                    "Software that manages computer hardware and resources",
                    "A programming language",
                    "A database",
                    "A web browser"
                ],
                "correct_answer": "Software that manages computer hardware and resources"
            },
            {
                "question": "Which is an example of an operating system?",
                "options": ["Linux", "MySQL", "Python", "HTML"],
                "correct_answer": "Linux"
            },
            {
                "question": "What is a process?",
                "options": [
                    "A program in execution",
                    "A file only",
                    "A CPU instruction only",
                    "A hardware component"
                ],
                "correct_answer": "A program in execution"
            },
            {
                "question": "Which component manages memory?",
                "options": [
                    "Operating system",
                    "Text editor",
                    "Compiler only",
                    "Browser"
                ],
                "correct_answer": "Operating system"
            },
        ],

        "Medium": [
            {
                "question": "What is a thread?",
                "options": [
                    "A lightweight unit of execution within a process",
                    "A hard disk",
                    "A database record",
                    "A compiler"
                ],
                "correct_answer": "A lightweight unit of execution within a process"
            },
            {
                "question": "Which scheduling algorithm gives each process a time slice?",
                "options": ["Round Robin", "FCFS", "SJF", "Priority only"],
                "correct_answer": "Round Robin"
            },
            {
                "question": "What is virtual memory?",
                "options": [
                    "A technique that uses disk space to extend apparent memory",
                    "A type of CPU",
                    "A cache only",
                    "A network protocol"
                ],
                "correct_answer": "A technique that uses disk space to extend apparent memory"
            },
            {
                "question": "What is a context switch?",
                "options": [
                    "Switching CPU execution from one process or thread to another",
                    "Changing files",
                    "Changing users",
                    "Changing programming languages"
                ],
                "correct_answer": "Switching CPU execution from one process or thread to another"
            },
        ],

        "Hard": [
            {
                "question": "Which condition is NOT one of the four Coffman conditions for deadlock?",
                "options": [
                    "Mutual exclusion",
                    "Hold and wait",
                    "Circular wait",
                    "Priority scheduling"
                ],
                "correct_answer": "Priority scheduling"
            },
            {
                "question": "What is a page fault?",
                "options": [
                    "An access to a page that is not currently in physical memory",
                    "A CPU failure",
                    "A disk formatting error",
                    "A process crash only"
                ],
                "correct_answer": "An access to a page that is not currently in physical memory"
            },
        ],
    },

    # =====================================================
    # COMPUTER NETWORKS
    # =====================================================
    "Computer Networks": {
        "Easy": [
            {
                "question": "What does LAN stand for?",
                "options": [
                    "Local Area Network",
                    "Large Access Network",
                    "Linked Area Node",
                    "Local Access Node"
                ],
                "correct_answer": "Local Area Network"
            },
            {
                "question": "Which device connects different networks?",
                "options": ["Router", "Keyboard", "Monitor", "Printer"],
                "correct_answer": "Router"
            },
            {
                "question": "Which protocol is used for web browsing?",
                "options": ["HTTP", "FTP", "SMTP", "SSH"],
                "correct_answer": "HTTP"
            },
            {
                "question": "What does IP stand for?",
                "options": [
                    "Internet Protocol",
                    "Internal Process",
                    "Internet Program",
                    "Input Protocol"
                ],
                "correct_answer": "Internet Protocol"
            },
        ],

        "Medium": [
            {
                "question": "Which transport protocol provides reliable, connection-oriented communication?",
                "options": ["UDP", "TCP", "IP", "ARP"],
                "correct_answer": "TCP"
            },
            {
                "question": "What is DNS used for?",
                "options": [
                    "Mapping domain names to IP addresses",
                    "Encrypting files",
                    "Sending email",
                    "Assigning MAC addresses"
                ],
                "correct_answer": "Mapping domain names to IP addresses"
            },
            {
                "question": "Which protocol is commonly used to send email?",
                "options": ["SMTP", "HTTP", "FTP", "DNS"],
                "correct_answer": "SMTP"
            },
            {
                "question": "Which layer of the OSI model handles routing?",
                "options": ["Network", "Transport", "Session", "Physical"],
                "correct_answer": "Network"
            },
        ],

        "Hard": [
            {
                "question": "What is the purpose of TCP's three-way handshake?",
                "options": [
                    "Establish a reliable connection",
                    "Encrypt HTTP data",
                    "Resolve domain names",
                    "Assign a MAC address"
                ],
                "correct_answer": "Establish a reliable connection"
            },
            {
                "question": "What is subnetting?",
                "options": [
                    "Dividing a network into smaller logical networks",
                    "Encrypting network traffic",
                    "Changing a MAC address",
                    "Creating DNS records"
                ],
                "correct_answer": "Dividing a network into smaller logical networks"
            },
            {
                "question": "Which protocol maps an IPv4 address to a MAC address on a local network?",
                "options": ["ARP", "DNS", "TCP", "DHCP"],
                "correct_answer": "ARP"
            },
        ],
    },

    # =====================================================
    # CLOUD COMPUTING
    # =====================================================
    "Cloud Computing": {
        "Easy": [
            {
                "question": "What is cloud computing?",
                "options": [
                    "Delivery of computing resources over a network",
                    "Only local storage",
                    "A programming language",
                    "A database model"
                ],
                "correct_answer": "Delivery of computing resources over a network"
            },
            {
                "question": "Which is a cloud service model?",
                "options": ["IaaS", "HTML", "CSS", "LAN"],
                "correct_answer": "IaaS"
            },
            {
                "question": "Which is an example of a cloud storage service?",
                "options": ["Google Drive", "Notepad", "Calculator", "Paint"],
                "correct_answer": "Google Drive"
            },
        ],

        "Medium": [
            {
                "question": "What does IaaS provide?",
                "options": [
                    "Virtualized computing infrastructure",
                    "Only source code",
                    "Only email",
                    "Only database queries"
                ],
                "correct_answer": "Virtualized computing infrastructure"
            },
            {
                "question": "What does PaaS provide?",
                "options": [
                    "A platform for developing and deploying applications",
                    "Only physical servers",
                    "Only network cables",
                    "Only storage devices"
                ],
                "correct_answer": "A platform for developing and deploying applications"
            },
            {
                "question": "What is elasticity in cloud computing?",
                "options": [
                    "Automatically adjusting resources according to demand",
                    "Encrypting data",
                    "Deleting servers",
                    "Creating user accounts"
                ],
                "correct_answer": "Automatically adjusting resources according to demand"
            },
        ],

        "Hard": [
            {
                "question": "What is multi-tenancy in cloud computing?",
                "options": [
                    "Multiple customers sharing a cloud infrastructure with logical isolation",
                    "Using multiple passwords",
                    "Running only one application",
                    "Using multiple monitors"
                ],
                "correct_answer": "Multiple customers sharing a cloud infrastructure with logical isolation"
            },
            {
                "question": "What is a hypervisor?",
                "options": [
                    "Software that creates and manages virtual machines",
                    "A database engine",
                    "A network cable",
                    "A programming language"
                ],
                "correct_answer": "Software that creates and manages virtual machines"
            },
        ],
    },

    # =====================================================
    # MACHINE LEARNING
    # =====================================================
    "Machine Learning": {
        "Easy": [
            {
                "question": "What is supervised learning?",
                "options": [
                    "Learning from labeled data",
                    "Learning without data",
                    "Only clustering",
                    "Only reinforcement"
                ],
                "correct_answer": "Learning from labeled data"
            },
            {
                "question": "Which is a classification algorithm?",
                "options": ["Logistic Regression", "K-Means", "PCA", "Apriori"],
                "correct_answer": "Logistic Regression"
            },
            {
                "question": "What is a feature?",
                "options": [
                    "An input variable used by a model",
                    "The final prediction only",
                    "A database table",
                    "A programming language"
                ],
                "correct_answer": "An input variable used by a model"
            },
            {
                "question": "Which learning method groups similar data points?",
                "options": ["Clustering", "Classification", "Regression", "Compilation"],
                "correct_answer": "Clustering"
            },
        ],

        "Medium": [
            {
                "question": "What is overfitting?",
                "options": [
                    "A model performs very well on training data but poorly on unseen data",
                    "A model has no features",
                    "A model cannot train",
                    "A model has too few samples only"
                ],
                "correct_answer": "A model performs very well on training data but poorly on unseen data"
            },
            {
                "question": "What does K-Means clustering attempt to minimize?",
                "options": [
                    "Within-cluster squared distances",
                    "Classification error only",
                    "Tree depth",
                    "Network latency"
                ],
                "correct_answer": "Within-cluster squared distances"
            },
            {
                "question": "What is a confusion matrix used for?",
                "options": [
                    "Evaluating classification predictions",
                    "Sorting data",
                    "Reducing image size",
                    "Creating clusters only"
                ],
                "correct_answer": "Evaluating classification predictions"
            },
            {
                "question": "What is cross-validation used for?",
                "options": [
                    "Estimating model performance on unseen data",
                    "Creating databases",
                    "Encrypting features",
                    "Increasing RAM"
                ],
                "correct_answer": "Estimating model performance on unseen data"
            },
        ],

        "Hard": [
            {
                "question": "What is regularization used for in machine learning?",
                "options": [
                    "Reducing overfitting by penalizing model complexity",
                    "Increasing dataset size",
                    "Deleting labels",
                    "Creating neural networks only"
                ],
                "correct_answer": "Reducing overfitting by penalizing model complexity"
            },
            {
                "question": "What is the purpose of a learning rate in gradient descent?",
                "options": [
                    "Controls the size of parameter updates",
                    "Controls dataset size",
                    "Controls number of classes",
                    "Controls CPU speed"
                ],
                "correct_answer": "Controls the size of parameter updates"
            },
            {
                "question": "What is precision in classification?",
                "options": [
                    "The fraction of predicted positives that are actually positive",
                    "The fraction of all samples that are positive",
                    "The fraction of negatives correctly predicted",
                    "The number of features"
                ],
                "correct_answer": "The fraction of predicted positives that are actually positive"
            },
        ],
    },

    # =====================================================
    # ARTIFICIAL INTELLIGENCE
    # =====================================================
    "Artificial Intelligence": {
        "Easy": [
            {
                "question": "What is Artificial Intelligence?",
                "options": [
                    "The field of creating systems capable of intelligent behavior",
                    "A database system",
                    "A web framework",
                    "A computer network"
                ],
                "correct_answer": "The field of creating systems capable of intelligent behavior"
            },
            {
                "question": "Which is an example of an AI application?",
                "options": [
                    "Voice assistant",
                    "Text file",
                    "Keyboard",
                    "USB cable"
                ],
                "correct_answer": "Voice assistant"
            },
            {
                "question": "What is an intelligent agent?",
                "options": [
                    "A system that perceives its environment and acts on it",
                    "A database table",
                    "A compiler",
                    "A network cable"
                ],
                "correct_answer": "A system that perceives its environment and acts on it"
            },
        ],

        "Medium": [
            {
                "question": "What is heuristic search?",
                "options": [
                    "Search guided by an estimate of how promising a state is",
                    "Random searching only",
                    "Database indexing",
                    "Network routing"
                ],
                "correct_answer": "Search guided by an estimate of how promising a state is"
            },
            {
                "question": "Which algorithm combines path cost and heuristic cost?",
                "options": ["A*", "BFS", "DFS", "Bubble Sort"],
                "correct_answer": "A*"
            },
            {
                "question": "What is knowledge representation?",
                "options": [
                    "Representing knowledge so an AI system can reason with it",
                    "Storing images only",
                    "Compressing files",
                    "Designing websites"
                ],
                "correct_answer": "Representing knowledge so an AI system can reason with it"
            },
        ],

        "Hard": [
            {
                "question": "What does an admissible heuristic guarantee for A* under standard conditions?",
                "options": [
                    "It never overestimates the true remaining cost",
                    "It always returns a random path",
                    "It removes all nodes",
                    "It makes the graph cyclic"
                ],
                "correct_answer": "It never overestimates the true remaining cost"
            },
            {
                "question": "What is the purpose of minimax in AI?",
                "options": [
                    "Choosing moves in adversarial games",
                    "Sorting arrays",
                    "Clustering data",
                    "Compressing images"
                ],
                "correct_answer": "Choosing moves in adversarial games"
            },
        ],
    },

    # =====================================================
    # CYBER SECURITY
    # =====================================================
    "Cyber Security": {
        "Easy": [
            {
                "question": "What is cybersecurity?",
                "options": [
                    "Protecting systems, networks, and data from attacks",
                    "Creating websites",
                    "Managing databases only",
                    "Designing hardware"
                ],
                "correct_answer": "Protecting systems, networks, and data from attacks"
            },
            {
                "question": "What does a firewall help control?",
                "options": [
                    "Network traffic",
                    "Screen brightness",
                    "Keyboard input",
                    "CPU temperature"
                ],
                "correct_answer": "Network traffic"
            },
            {
                "question": "What is phishing?",
                "options": [
                    "A deceptive attempt to obtain sensitive information",
                    "A database technique",
                    "A compression method",
                    "A sorting algorithm"
                ],
                "correct_answer": "A deceptive attempt to obtain sensitive information"
            },
            {
                "question": "What is encryption?",
                "options": [
                    "Converting readable data into protected encoded form",
                    "Deleting data",
                    "Compressing only images",
                    "Creating a database"
                ],
                "correct_answer": "Converting readable data into protected encoded form"
            },
        ],

        "Medium": [
            {
                "question": "What is SQL injection?",
                "options": [
                    "An attack that manipulates SQL queries through untrusted input",
                    "A network cable failure",
                    "A password hashing algorithm",
                    "A backup method"
                ],
                "correct_answer": "An attack that manipulates SQL queries through untrusted input"
            },
            {
                "question": "What is authentication?",
                "options": [
                    "Verifying the identity of a user or system",
                    "Granting permissions only",
                    "Encrypting a database",
                    "Deleting accounts"
                ],
                "correct_answer": "Verifying the identity of a user or system"
            },
            {
                "question": "What is authorization?",
                "options": [
                    "Determining what an authenticated user is allowed to access",
                    "Verifying identity",
                    "Creating passwords",
                    "Encrypting traffic"
                ],
                "correct_answer": "Determining what an authenticated user is allowed to access"
            },
            {
                "question": "What is hashing commonly used for?",
                "options": [
                    "Creating fixed-size representations such as password hashes",
                    "Sending emails",
                    "Routing packets",
                    "Rendering web pages"
                ],
                "correct_answer": "Creating fixed-size representations such as password hashes"
            },
        ],

        "Hard": [
            {
                "question": "What is XSS?",
                "options": [
                    "A vulnerability involving execution of attacker-controlled script in a user's browser",
                    "A database backup technique",
                    "A network routing protocol",
                    "An encryption algorithm"
                ],
                "correct_answer": "A vulnerability involving execution of attacker-controlled script in a user's browser"
            },
            {
                "question": "What is the principle of least privilege?",
                "options": [
                    "Giving users only the permissions necessary for their tasks",
                    "Giving every user administrator access",
                    "Removing authentication",
                    "Encrypting every file"
                ],
                "correct_answer": "Giving users only the permissions necessary for their tasks"
            },
            {
                "question": "What is multi-factor authentication?",
                "options": [
                    "Authentication using two or more different types of factors",
                    "Using multiple usernames",
                    "Using multiple browsers",
                    "Using one password twice"
                ],
                "correct_answer": "Authentication using two or more different types of factors"
            },
        ],
    },
}


# ---------------------------------------------------------
# EXTRA QUESTION GENERATION
# ---------------------------------------------------------

def normalize_question(question):
    """
    Makes sure every question has the same structure.
    """
    return {
        "question": str(question.get("question", "")),
        "options": list(question.get("options", [])),
        "correct_answer": str(question.get("correct_answer", "")),
    }


def get_local_questions(category, difficulty, question_count):
    """
    Returns questions ONLY from the selected category
    and selected difficulty.

    If the requested difficulty does not have enough questions,
    questions from the other difficulty levels of the SAME
    category are used as a fallback.
    """

    category_data = QUESTION_BANK.get(category)

    if not category_data:
        category_data = QUESTION_BANK["Python"]

    selected_questions = list(
        category_data.get(difficulty, [])
    )

    # If the selected difficulty has fewer questions,
    # use the other difficulty levels from the SAME category.
    if len(selected_questions) < question_count:

        for other_difficulty in ["Easy", "Medium", "Hard"]:

            if other_difficulty == difficulty:
                continue

            selected_questions.extend(
                category_data.get(other_difficulty, [])
            )

            if len(selected_questions) >= question_count:
                break

    # Remove duplicate question text.
    unique_questions = {}

    for item in selected_questions:
        normalized = normalize_question(item)
        unique_questions[normalized["question"]] = normalized

    selected_questions = list(unique_questions.values())

    # Randomize question order.
    random.shuffle(selected_questions)

    return selected_questions[:question_count]


# ---------------------------------------------------------
# OPENAI GENERATION
# ---------------------------------------------------------

def generate_with_openai(category, difficulty, question_count):
    """
    Attempts to generate questions using OpenAI.

    If OpenAI is unavailable or has no credits,
    the application automatically uses the local
    category-specific question bank.
    """

    if not OPENAI_API_KEY:
        return None

    try:
        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = f"""
Create exactly {question_count} multiple-choice questions.

Category:
{category}

Difficulty:
{difficulty}

IMPORTANT:
- Every question MUST be specifically about {category}.
- Do NOT generate questions from another programming language,
  technology, or unrelated CSE topic.
- Questions must be different from each other.
- Each question must have exactly 4 options.
- Only one option must be correct.
- Questions should be suitable for a B.Tech CSE student.

Return ONLY valid JSON in this exact format:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "correct_answer": "Option A"
        }}
    ]
}}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert CSE quiz generator. "
                        "Always follow the requested category exactly."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0.8,
        )

        content = response.choices[0].message.content.strip()

        # Remove markdown JSON fences if returned by the model.
        if content.startswith("```"):
            content = content.replace("```json", "")
            content = content.replace("```", "")
            content = content.strip()

        parsed = json.loads(content)

        questions = parsed.get("questions", [])

        if not isinstance(questions, list):
            return None

        cleaned = []

        for item in questions:
            if not isinstance(item, dict):
                continue

            question_text = str(
                item.get("question", "")
            ).strip()

            options = item.get("options", [])

            correct_answer = str(
                item.get("correct_answer", "")
            ).strip()

            if (
                question_text
                and isinstance(options, list)
                and len(options) == 4
                and correct_answer
            ):
                cleaned.append(
                    {
                        "question": question_text,
                        "options": [
                            str(option)
                            for option in options
                        ],
                        "correct_answer": correct_answer,
                    }
                )

        if len(cleaned) >= question_count:
            return cleaned[:question_count]

    except Exception as error:
        print(
            "OpenAI generation failed. "
            "Using local category question bank."
        )
        print("Reason:", error)

    return None


# ---------------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------------

def generate_quiz(
    category="Python",
    difficulty="Medium",
    question_count=20,
):
    """
    Main quiz-generation function used by main.py.

    Priority:
    1. OpenAI category-specific generation
    2. Local category-specific question bank
    """

    if category not in QUESTION_BANK:
        category = "Python"

    if difficulty not in DIFFICULTIES:
        difficulty = "Medium"

    try:
        question_count = int(question_count)
    except (TypeError, ValueError):
        question_count = 20

    if question_count not in [10, 15, 20]:
        question_count = 20

    # Try AI generation first.
    ai_questions = generate_with_openai(
        category,
        difficulty,
        question_count,
    )

    if ai_questions:
        return ai_questions

    # Local category-specific fallback.
    return get_local_questions(
        category,
        difficulty,
        question_count,
    )


# ---------------------------------------------------------
# SUPPORTED DIFFICULTIES
# ---------------------------------------------------------

DIFFICULTIES = [
    "Easy",
    "Medium",
    "Hard",
]
def generate_quiz_questions(
    category="Python",
    difficulty="Medium",
    count=20,
):
    return generate_quiz(
        category=category,
        difficulty=difficulty,
        question_count=count,
    )