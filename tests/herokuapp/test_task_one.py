from front_end import frames_elements
from front_end.frames_elements import BasePageElements, NestedFramesElements


class TestTaskOne:
    def test_select_nested_frames(self):
        frames_elements.select_page(BasePageElements.frames_link)
        frames_elements.select_page(BasePageElements.nexted_frames_link)

    def test_print_top_frame_text(self):
        frames_elements.switch_to_frame(NestedFramesElements.frame_top)
        frames_elements.switch_to_frame(NestedFramesElements.frame_middle)
        print(frames_elements.print_frame_text('MIDDLE'))

        frames_elements.switch_to_parents_frame(2)
        frames_elements.switch_to_frame(NestedFramesElements.frame_bottom)
        print(frames_elements.print_frame_text('BOTTOM'))

        frames_elements.switch_to_parents_frame()
        frames_elements.switch_to_frame(NestedFramesElements.frame_top)
        frames_elements.switch_to_frame(NestedFramesElements.frame_left)
        print(frames_elements.print_frame_text('LEFT'))

        frames_elements.switch_to_parents_frame()
        frames_elements.switch_to_frame(NestedFramesElements.frame_right)
        print(frames_elements.print_frame_text('RIGHT'))
