import requests 
from bs4 import BeautifulSoup
import csv
from collections.abc import Mapping
import re
from requests import get
import sys
import time
import random
from requests.adapters import HTTPAdapter, Retry
from transformers import AutoTokenizer, logging 
import torch
from transformers import AutoModel
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import statistics
import json
import os
from flask import send_from_directory, request, jsonify, make_response
