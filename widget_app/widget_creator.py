class Widget:
    def __init__(self):
        self._name = "Widget"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


def create_widget():
    return Widget()


def user_can_get_widget(user_id):
    return True


def issue_widget(user_id):
    from pytest_mock_bug_repro.widget_utils import rotate_widget

    if user_can_get_widget(user_id):
        ret = create_widget()
        return rotate_widget(ret)
    else:
        raise Exception("User cannot get widget")


def issue_widget_with_name(user_id, name):
    from pytest_mock_bug_repro.widget_utils import create_widget_with_name

    if user_can_get_widget(user_id):
        ret = create_widget_with_name(name)
        return ret
    else:
        raise Exception("User cannot get widget")
