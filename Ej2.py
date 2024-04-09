import numpy as np

def is_inverse(A: np.ndarray, B: np.ndarray, k):
    n = A.shape[0]
    for _ in range(k):
        v = np.random.rand(n, 1)
        
        Av = np.dot(A, v)
        BAv = np.dot(B, Av)
        
        dif = np.linalg.norm(v - BAv)
        
        if dif > 1e-6:
            return False
        
    # Si todas las iteraciones pasan, retornar True  
    return True

def is_inverse_aux(A: np.ndarray, B: np.ndarray, epsilon):
    n = A.shape[0]
    for _ in range(int(np.log(1/epsilon))):
        v = np.random.rand(n, 1)
        
        Av = np.dot(A, v)
        BAv = np.dot(B, Av)
        
        dif = np.linalg.norm(v - BAv)
        
        if dif > epsilon:
            return False
            
    # Si todas las iteraciones pasan, retornar True
    return True
