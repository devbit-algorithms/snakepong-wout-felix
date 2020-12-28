import turtle


class Tail:

    def add_tail(self, segments):
        tail_segment = turtle.Turtle()
        tail_segment.speed(0)
        tail_segment.shape("square")
        tail_segment.color("grey")
        tail_segment.penup()
        segments.append(tail_segment)
        return segments

        