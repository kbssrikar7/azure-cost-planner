"""
Azure Cloud Cost Planner - Streamlit Application
Main application for estimating Azure Virtual Machine costs.
"""

import streamlit as st
from data.prices import (
    get_hourly_price,
    get_all_regions_for_vm,
    format_region_name,
    AVAILABLE_REGIONS,
    AVAILABLE_VM_SIZES,
)
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Azure Cloud Cost Planner",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for sticky inputs
if "last_region" not in st.session_state:
    st.session_state.last_region = AVAILABLE_REGIONS[0] if AVAILABLE_REGIONS else ""
if "last_vm_size" not in st.session_state:
    st.session_state.last_vm_size = AVAILABLE_VM_SIZES[0] if AVAILABLE_VM_SIZES else ""
if "last_os" not in st.session_state:
    st.session_state.last_os = "Linux"
if "last_hours" not in st.session_state:
    st.session_state.last_hours = 730
if "currency" not in st.session_state:
    st.session_state.currency = "INR"


def calculate_monthly_cost(hourly_price: float, hours_per_month: int) -> float:
    """Calculate monthly cost from hourly price and hours per month."""
    return hourly_price * hours_per_month


def main():
    """Main application entry point."""
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 1rem;
        }
        .cost-card {
            background-color: #f0f2f6;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #1f77b4;
            margin: 1rem 0;
            color: #262730;
        }
        .cost-card h3 {
            color: #1f77b4;
            margin-top: 0;
        }
        .cost-card p {
            color: #262730;
            margin: 0.5rem 0;
        }
        .cost-card ul {
            color: #262730;
        }
        .cost-card li {
            color: #262730;
        }
        .cost-card hr {
            border-color: #1f77b4;
            opacity: 0.3;
        }
        .warning-box {
            background-color: #fff3cd;
            padding: 1rem;
            border-radius: 5px;
            border-left: 5px solid #ffc107;
            margin: 1rem 0;
            color: #856404;
        }
        .warning-box h4 {
            color: #856404;
            margin-top: 0;
        }
        .warning-box p {
            color: #856404;
            margin: 0.5rem 0;
        }
        .warning-box ul {
            color: #856404;
        }
        .warning-box li {
            color: #856404;
        }
        .footer {
            text-align: center;
            color: #666;
            padding: 2rem 0;
            margin-top: 3rem;
            border-top: 1px solid #ddd;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<p class="main-header">☁️ Azure Cloud Cost Planner</p>', unsafe_allow_html=True)
    
    # Currency selector in sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        st.session_state.currency = st.radio(
            "Currency",
            ["INR", "USD"],
            index=0 if st.session_state.currency == "INR" else 1,
            help="Currency display (values are illustrative)"
        )
        st.caption("ℹ️ Currency values are illustrative")
    
    # Main tabs
    tab1, tab2, tab3 = st.tabs(["💰 Plan Cost", "🌍 Compare Regions", "ℹ️ About"])
    
    # Tab 1: Plan Cost (Estimator)
    with tab1:
        st.header("Plan Your Azure VM Cost")
        st.markdown("Configure your Virtual Machine and get an instant cost estimate.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Configuration")
            
            # Service (fixed for MVP)
            st.text_input(
                "Service",
                value="Virtual Machines",
                disabled=True,
                help="Currently only Virtual Machines are supported"
            )
            
            # Region dropdown
            region = st.selectbox(
                "Region",
                options=AVAILABLE_REGIONS,
                index=AVAILABLE_REGIONS.index(st.session_state.last_region) if st.session_state.last_region in AVAILABLE_REGIONS else 0,
                format_func=format_region_name,
                help="Select Azure region"
            )
            st.session_state.last_region = region
            
            # VM Size dropdown
            vm_size = st.selectbox(
                "VM Size",
                options=AVAILABLE_VM_SIZES,
                index=AVAILABLE_VM_SIZES.index(st.session_state.last_vm_size) if st.session_state.last_vm_size in AVAILABLE_VM_SIZES else 0,
                help="Select Virtual Machine size"
            )
            st.session_state.last_vm_size = vm_size
            
            # OS selection
            os = st.radio(
                "Operating System",
                options=["Linux", "Windows"],
                index=0 if st.session_state.last_os == "Linux" else 1,
                help="Select operating system"
            )
            st.session_state.last_os = os
            
            # Hours per month
            hours_per_month = st.number_input(
                "Hours per Month",
                min_value=1,
                max_value=744,
                value=st.session_state.last_hours,
                step=1,
                help="Number of hours the VM will run per month (max 744)"
            )
            st.session_state.last_hours = hours_per_month
            
            # Calculate button
            calculate_btn = st.button("💰 Calculate Cost", type="primary", use_container_width=True)
        
        with col2:
            st.subheader("Cost Estimate")
            
            if calculate_btn:
                # Look up hourly price
                hourly_price = get_hourly_price(region, vm_size, os)
                
                if hourly_price is not None:
                    # Calculate monthly cost: hourly_price × hours_per_month
                    # Example: 0.012 INR/hour × 730 hours = 8.76 INR/month
                    monthly_cost = calculate_monthly_cost(hourly_price, hours_per_month)
                    
                    # Display results in a card
                    st.markdown(f"""
                        <div class="cost-card">
                            <h3>📊 Cost Breakdown</h3>
                            <hr>
                            <p><strong>Hourly Price:</strong> {st.session_state.currency} {hourly_price:.4f} per hour</p>
                            <p><strong>Monthly Estimate:</strong> {st.session_state.currency} {monthly_cost:.2f}</p>
                            <hr>
                            <p><strong>Assumptions:</strong></p>
                            <ul>
                                <li>Region: {format_region_name(region)}</li>
                                <li>VM Size: {vm_size}</li>
                                <li>OS: {os}</li>
                                <li>Hours/Month: {hours_per_month}</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.success("✅ Cost calculated successfully!")
                    
                    # Additional info
                    with st.expander("ℹ️ Notes"):
                        st.markdown("""
                        - Prices are illustrative and may differ from Azure's live calculator
                        - This is an educational demo with a limited internal price catalog
                        - Future versions will integrate with Azure Retail Prices API
                        - Currency values are for display purposes only
                        """)
                else:
                    # Price not found
                    st.markdown(f"""
                        <div class="warning-box">
                            <h4>⚠️ Configuration Not Found</h4>
                            <p>The selected combination of region, VM size, and OS is not available in our price catalog.</p>
                            <p><strong>Suggestions:</strong></p>
                            <ul>
                                <li>Try a different region</li>
                                <li>Select a different VM size</li>
                                <li>Check if the OS option is correct</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("👈 Configure your VM settings on the left and click 'Calculate Cost' to see your estimate.")
    
    # Tab 2: Compare Regions
    with tab2:
        st.header("Compare Costs Across Regions")
        st.markdown("Compare the same VM configuration across different Azure regions.")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            compare_vm_size = st.selectbox(
                "VM Size",
                options=AVAILABLE_VM_SIZES,
                key="compare_vm_size",
                help="Select Virtual Machine size to compare"
            )
        
        with col2:
            compare_os = st.radio(
                "Operating System",
                options=["Linux", "Windows"],
                key="compare_os",
                help="Select operating system"
            )
        
        with col3:
            compare_hours = st.number_input(
                "Hours per Month",
                min_value=1,
                max_value=744,
                value=730,
                step=1,
                key="compare_hours",
                help="Number of hours per month"
            )
        
        if st.button("🌍 Compare Regions", type="primary"):
            # Get prices for all regions
            region_prices = get_all_regions_for_vm(compare_vm_size, compare_os)
            
            if region_prices:
                # Create DataFrame for display
                comparison_data = []
                for region, hourly_price in region_prices.items():
                    monthly_cost = calculate_monthly_cost(hourly_price, compare_hours)
                    comparison_data.append({
                        "Region": format_region_name(region),
                        "Hourly Price": f"{st.session_state.currency} {hourly_price:.4f}",
                        "Monthly Estimate": f"{st.session_state.currency} {monthly_cost:.2f}",
                        "Hourly (numeric)": hourly_price  # For sorting/charting
                    })
                
                df = pd.DataFrame(comparison_data)
                # Sort by hourly price
                df = df.sort_values("Hourly (numeric)")
                
                # Display table
                st.subheader("Regional Price Comparison")
                display_df = df[["Region", "Hourly Price", "Monthly Estimate"]].copy()
                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True
                )
                
                # Bar chart
                st.subheader("Price Comparison Chart")
                chart_df = df[["Region", "Hourly (numeric)"]].copy()
                chart_df = chart_df.rename(columns={"Hourly (numeric)": f"Hourly Price ({st.session_state.currency})"})
                st.bar_chart(chart_df.set_index("Region"), use_container_width=True)
                
                # Summary
                cheapest_region = df.iloc[0]["Region"]
                most_expensive_region = df.iloc[-1]["Region"]
                st.info(f"💡 **Cheapest:** {cheapest_region} | **Most Expensive:** {most_expensive_region}")
            else:
                st.warning("⚠️ No pricing data found for the selected VM size and OS combination.")
    
    # Tab 3: About
    with tab3:
        st.header("About This Project")
        
        st.markdown("""
        ### Project Title
        **Integrating Azure Pricing Calculator for Cloud Resource Planning and Cost Estimation**
        
        ---
        
        ### Project Overview
        
        This is an educational prototype designed to demonstrate cloud resource cost estimation 
        using Azure Virtual Machines as a use case. The application provides a web-based interface 
        for planning and estimating monthly costs for Azure VM deployments.
        
        ### Current Implementation
        
        - **Data Source**: Internal price catalog with illustrative pricing data
        - **Scope**: ~6-8 VM sizes across 4-5 Azure regions
        - **Services**: Virtual Machines (MVP)
        
        ### Important Notes
        
        ⚠️ **This is an educational demo.** Prices shown are illustrative and may differ significantly 
        from Azure's live pricing calculator and actual Azure retail prices.
        
        ### Future Enhancements
        
        - **Azure Retail Prices API Integration**: Replace internal catalog with real-time pricing from Azure
        - **Expanded Services**: Support for additional Azure services (Storage, Networking, etc.)
        - **Historical Trends**: Track price changes over time
        - **Advanced Features**: Reserved instances, spot pricing, cost optimization recommendations
        
        ### Deployment
        
        This application is designed to run on **Microsoft Azure App Service** (Free/F1 tier) 
        for zero-cost hosting during development and demonstration.
        
        ### Technology Stack
        
        - **Framework**: Streamlit
        - **Language**: Python 3.10+
        - **Data Processing**: Pandas
        - **Visualization**: Streamlit native charts
        - **Hosting**: Azure App Service (Linux)
        
        ---
        
        ### Project Team Details
        
        - **Professor**: Prof Ramesh C
        - **Students**: 
          - K.B.S Srikar
          - Dinesh Reddy
        - **Course**: Cloud Computing
        - **Institution**: Vellore Institute of Technology Vellore
        """)
    
    # Footer
    st.markdown("""
        <div class="footer">
            <p>Educational demo. Prices are illustrative and may differ from Azure's live calculator.</p>
            <p>Built with Streamlit ☁️</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

