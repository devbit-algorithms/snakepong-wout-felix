import turtle


class Tail:
    def __init__(self):
        self.start_tail_var = 1
    def add_tail(self, segments):
        tail_segment = turtle.Turtle()
        tail_segment.speed(0)
        tail_segment.shape("square")
        tail_segment.color("grey")
        tail_segment.penup()
        segments.append(tail_segment)
        return segments

    def start_tail(self, segments):
        if self.start_tail_var == 1:
                for i in range(0,3):
                    segments = self.add_tail(segments)
                self.start_tail_var = 2
        return segments
    def clear_start_tail_var(self):
        self.start_tail_var = 1