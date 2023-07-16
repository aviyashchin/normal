import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Use streamlit sliders to select means
mu1 = st.slider('Mean of first normal curve', min_value=-10.0, max_value=10.0, value=0.0)
mu2 = st.slider('Mean of second normal curve', min_value=-10.0, max_value=10.0, value=1.0)

# Fixed standard deviations for this example
sigma1 = sigma2 = 1.0

# Calculate PDFs
x = np.linspace(-10, 10, 1000)
pdf1 = norm.pdf(x, mu1, sigma1)
pdf2 = norm.pdf(x, mu2, sigma2)

# Plot the PDFs
plt.figure(figsize=(10, 6))
plt.plot(x, pdf1, label=f'N({mu1}, {sigma1})')
plt.plot(x, pdf2, label=f'N({mu2}, {sigma2})')
plt.legend()
plt.title('Comparison of Two Normal Curves')
plt.xlabel('Value')
plt.ylabel('Probability Density')
st.pyplot(plt)
