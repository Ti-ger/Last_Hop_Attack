FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python lasthop_anonymity_sets.py; python lasthop_advantage_uniform_cascade_selection.py; python lasthop_advantage_bandwidth_based_cascade_selection.py
