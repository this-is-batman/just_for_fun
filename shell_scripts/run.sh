#!/bin/bash
python ./src/optim_power.py
pytest -v

# now, we need to run the dashboard
streamlit run streamlit_dashboard.py --server.port 18000 --server.address 0.0.0.0