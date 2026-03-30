def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    # Ensure everything is a numpy array for element-wise math
    param, grad, m, v = np.asarray(param), np.asarray(grad), np.asarray(m), np.asarray(v)
    
    # Now math works:
    m_new = beta1 * m + (1 - beta1) * grad
    
    # 2. Update biased second raw moment estimate (uncentered variance)
    v_new = beta2 * v + (1 - beta2) * (grad**2)
    
    # 3. Compute bias-corrected first moment estimate
    # t is the current timestep (1, 2, 3...)
    m_hat = m_new / (1 - beta1**t)
    
    # 4. Compute bias-corrected second raw moment estimate
    v_hat = v_new / (1 - beta2**t)
    
    # 5. Update parameters
    # The epsilon (eps) prevents division by zero
    param_new = param - lr * m_hat / (np.sqrt(v_hat) + eps)
    
    return param_new, m_new, v_new
