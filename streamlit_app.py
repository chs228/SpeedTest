import streamlit as st
import speedtest
import plotly.graph_objects as go

def test_speed():
    """Function to test internet speed."""
    st.info("Testing internet speed. Please wait...")
    try:
        stt = speedtest.Speedtest()
        stt.get_best_server()
        download_speed = stt.download() / 1e6  # Convert to Mbps
        upload_speed = stt.upload() / 1e6  # Convert to Mbps
        ping = stt.results.ping
        
        return {
            "Download Speed (Mbps)": round(download_speed, 2),
            "Upload Speed (Mbps)": round(upload_speed, 2),
            "Ping (ms)": round(ping, 2)
        }
    except Exception as e:
        st.error(f"Error occurred while testing speed: {e}")
        return None

def create_speedometer(value, title, max_value):
    """Create a speedometer-style gauge."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={
            'axis': {'range': [0, max_value]},
            'bar': {'color': "blue"},
            'steps': [
                {'range': [0, max_value * 0.5], 'color': "lightgray"},
                {'range': [max_value * 0.5, max_value * 0.8], 'color': "gray"},
                {'range': [max_value * 0.8, max_value], 'color': "green"}
            ],
        }
    ))
    return fig

# Streamlit UI
st.title("Internet Speed Test")
st.write("Check your internet speed using this app.")

if st.button("Run Speed Test"):
    results = test_speed()
    if results:
        st.success("Speed Test Results:")

        # Download Speedometer
        st.plotly_chart(create_speedometer(
            results['Download Speed (Mbps)'],
            "Download Speed (Mbps)",
            max_value=200  # Adjust max_value based on expected speeds
        ))

        # Upload Speedometer
        st.plotly_chart(create_speedometer(
            results['Upload Speed (Mbps)'],
            "Upload Speed (Mbps)",
            max_value=50  # Adjust max_value based on expected speeds
        ))

        # Ping Speedometer
        st.plotly_chart(create_speedometer(
            results['Ping (ms)'],
            "Ping (ms)",
            max_value=100  # Adjust max_value based on expected range
        ))
    else:
        st.error("Failed to fetch speed test results.")
