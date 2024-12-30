import streamlit as st
import speedtest

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

# Streamlit UI
st.title("Internet Speed Test")
st.write("Check your internet speed using this app.")

if st.button("Run Speed Test"):
    results = test_speed()
    if results:
        st.success("Speed Test Results:")
        st.metric(label="Download Speed", value=f"{results['Download Speed (Mbps)']} Mbps")
        st.metric(label="Upload Speed", value=f"{results['Upload Speed (Mbps)']} Mbps")
        st.metric(label="Ping", value=f"{results['Ping (ms)']} ms")
    else:
        st.error("Failed to fetch speed test results.")
