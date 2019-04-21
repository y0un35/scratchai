"""
Semantic adversarial Examples
"""

# FIXME Change this from class to function
class Semantic():
  """
  Semantic adversarial examples.
  
  https://arxiv.org/abs/1703.06857

  Note: data must either be centered (so that the negative image can be
  made by simple negation) or must be in the interval of [-1, 1]

  Arguments
  ---------
  net : nn.Module, optional
        The model on which to perform the attack.
  center : bool
           If true, assumes data has 0 mean so the negative image is just negation.
           If false, assumes data is in interval [0, max_val]
  max_val : float
            Maximum value allowed in the input data.
  kwargs : dict, optional
           Any additional arguments
  """

  def __init__(self, net, center:bool=True, max_val:float=1., **kwargs):
    super().__init__(net, **kwargs)
    self.center = center
    self.max_val = max_val

  def generate(self, x, **kwargs):
    if self.center:
      return x*-1
    return self.max_val - x
