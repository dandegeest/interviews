from dataclasses import dataclass


@dataclass
class FooBar:
    foo: str = "foo"
    bar: str = "bar"
    baz: str = "baz"
    name: str = "Dan"
    
    def hello() -> str:
        return f"My name is {get_name()}"

def get_foo() -> str:
    return FooBar.foo

def get_bar() -> str:
    return FooBar.bar

def get_baz() -> str:
    return FooBar.baz

def get_name() -> str:
    return FooBar.name

if __name__ == "__main__":
    print("\n\nHello World!")
    print(FooBar.hello())
