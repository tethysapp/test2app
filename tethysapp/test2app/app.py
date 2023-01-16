from tethys_sdk.base import TethysAppBase


class Test2App(TethysAppBase):
    """
    Tethys app class for Test2App.
    """

    name = 'Test2App'
    description = ''
    package = 'test2app'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'test2app'
    color = '#2c3e50'
    tags = ''
    enable_feedback = False
    feedback_emails = []