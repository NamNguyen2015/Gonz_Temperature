import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Bar Plot with Cursor")
    fig, ax = plt.subplots()
    ax.bar(range(9), range(1, 10), align="center")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    # Plotting the figure
    st.pyplot(fig)

    # Add text box for cursor display
    st.text("Hover over the bars to display their values.")

if __name__ == "__main__":
    main()