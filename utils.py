
# plots piecewise growth function
# A and B should be valid input to piecewise.make_piecewise

def plot_piecewise(A: List[float], B: List[float]):
  import matplotlib.pyplot as plt
  
  plt.plot([A[0], A[-1]], [A[0], A[-1]], color="red", label="id")
  plt.plot([A[0], A[1]], [B[0], B[0]], color="blue", label="growth")
  for i in range(1, len(B)):
    plt.plot([A[i], A[i]], [B[i-1], B[i]], ":", color="blue")
    plt.plot([A[i], A[i+1]], [B[i], B[i]], color="blue")
    
  plt.xticks(A + B)
  plt.yticks(A + B)
  plt.legend()
  plt.show()
