from unittest.mock import patch

import pytest

from widget_app.widget_creator import issue_widget, issue_widget_with_name


@patch("pytest_mock_bug_repro.widget_creator.create_widget")
@patch("pytest_mock_bug_repro.widget_creator.user_can_get_widget")
def test_issue_widget(
    mock_user_can_get_widget,
    mock_create_widget,
):
    mock_user_can_get_widget.return_value = False
    mock_create_widget.return_value = "mock widget"

    with pytest.raises(Exception):
        issue_widget("user_id")


# We want to use the real create_widget function here, not the mock
@patch("pytest_mock_bug_repro.widget_creator.user_can_get_widget")
def test_issue_widget_with_name(mock_user_can_get_widget):
    mock_user_can_get_widget.return_value = True
    widget = issue_widget_with_name("user_id", "name")
    assert widget.get_name() == "name"
