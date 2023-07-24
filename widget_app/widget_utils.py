from widget_app.widget_creator import Widget, create_widget

print("widget_utils first imported")


def rotate_widget(widget: Widget):
    print("Rotating widget")
    # <very import rotation code here>
    return widget


def create_widget_with_name(name: str):
    print("Creating widget with name")
    widget = create_widget()
    widget.set_name(name)
    return widget
