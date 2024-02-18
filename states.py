#!/usr/bin/python3
import typing


class Transition:
    def __init__(self, condition: typing.Callable[[str], bool],
                 target_state: "State"):
        self.condition = condition
        self.target_state = target_state


class State:
    def __init__(self, name: str = None, parent: "State" = None,
                 initial: bool = False, final: bool = False):
        self.name = name
        self.states: list[State] = []
        self.transitions: list[Transition] = []
        self.active = False
        self.initial = initial
        self.final = final

        if parent:
            parent.states += [self]

    def on_entry(self) -> None:
        print("{} entered".format(self.name))

    def on_exit(self) -> None:
        print("{} exited".format(self.name))

    def set(self, active: bool) -> None:
        if self.active == active:
            return

        if active:
            self.on_entry()
        else:
            self.on_exit()

        self.active = active
        # Propergate
        for s in self.states:
            if (s.initial and active) or (s.final and not active):
                s.set(True)

    def event(self, name: str) -> None:
        if self.active:
            # Jump
            for t in self.transitions:
                if t.condition(name):
                    t.target_state.set(True)
                    self.set(False)
                    return
            # Propergate
            for s in self.states:
                s.event(name)


if __name__ == '__main__':
    # states
    root = State()
    one = State("one", root, True)
    two = State("two", root)

    # transitions
    one.transitions += [Transition(lambda event: event == "inc", two)]
    two.transitions += [Transition(lambda event: event == "dec", one)]

    # events
    event = ["inc",  "dec"]

    # start
    root.set(True)

    while True:
        for i, e in enumerate(event):
            print(f"{i+1}:{e}")
        key = input("Select an event or press 'q' to quit")
        if key == 'q':
            break
        elif key.isdigit():
            e = event[int(key)-1]
            print(e)
            root.event(e)
