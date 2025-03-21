
class Finally:
  def __init__(self, action_on_destruction):
    self.action_on_destruction = action_on_destruction

  def __del__(self):
    self.action_on_destruction()
