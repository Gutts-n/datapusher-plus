# encoding: utf-8
# flake8: noqa: E501

import json
import requests
from pathlib import Path
import os
import ckan.plugins.toolkit as tk

# SSL verification settings
SSL_VERIFY = tk.asbool(os.environ.get("CKAN___SSL_VERIFY"))
if not SSL_VERIFY:
    requests.packages.urllib3.disable_warnings()

# Proxy settings
USE_PROXY = "CKANEXT__DATAPUSHER_PLUS__DOWNLOAD_PROXY" in os.environ
if USE_PROXY:
    DOWNLOAD_PROXY = os.environ.get("CKANEXT__DATAPUSHER_PLUS__DOWNLOAD_PROXY")

# PostgreSQL integer limits
POSTGRES_INT_MAX = 2147483647
POSTGRES_INT_MIN = -2147483648
POSTGRES_BIGINT_MAX = 9223372036854775807
POSTGRES_BIGINT_MIN = -9223372036854775808

# QSV version requirements
MINIMUM_QSV_VERSION = "4.0.0"

# Logging level
# TRACE, DEBUG, INFO, WARNING, ERROR, CRITICAL
UPLOAD_LOG_LEVEL = os.environ.get("CKANEXT__DATAPUSHER_PLUS__UPLOAD_LOG_LEVEL", "INFO")

# Supported formats
FORMATS = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__FORMATS",
    ["csv", "tsv", "tab", "ssv", "xls", "xlsx", "ods", "geojson", "shp", "qgis", "zip"],
)
if isinstance(FORMATS, str):
    FORMATS = FORMATS.split()

# PII screening settings
PII_SCREENING = tk.asbool(os.environ.get("CKANEXT__DATASTORE_PLUS__PII_SCREENING", "False"))
PII_FOUND_ABORT = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__PII_FOUND_ABORT", "False")
)
PII_REGEX_RESOURCE_ID = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__PII_REGEX_RESOURCE_ID_OR_ALIAS"
)
PII_SHOW_CANDIDATES = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__PII_SHOW_CANDIDATES", "False")
)
PII_QUICK_SCREEN = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__PII_QUICK_SCREEN", "False")
)

# Binary paths
QSV_BIN = Path(os.environ.get("CKANEXT__DATAPUSHER_PLUS__QSV_BIN"))

# Data processing settings
PREVIEW_ROWS = tk.asint(os.environ.get("CKANEXT__DATAPUSHER_PLUS__PREVIEW_ROWS", "1000"))
TIMEOUT = tk.asint(os.environ.get("CKANEXT__DATAPUSHER_PLUS__DOWNLOAD_TIMEOUT", "300"))
MAX_CONTENT_LENGTH = tk.asint(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__MAX_CONTENT_LENGTH", "5000000")
)
CHUNK_SIZE = tk.asint(os.environ.get("CKANEXT__DATAPUSHER_PLUS__CHUNK_SIZE", "1048576"))
DEFAULT_EXCEL_SHEET = tk.asint(os.environ.get("CKAN___DEFAULT_EXCEL_SHEET", "0"))
SORT_AND_DUPE_CHECK = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__SORT_AND_DUPE_CHECK", "True")
)
DEDUP = tk.asbool(os.environ.get("CKANEXT__DATAPUSHER_PLUS__DEDUP", "True"))
UNSAFE_PREFIX = os.environ.get("CKANEXT__DATAPUSHER_PLUS__UNSAFE_PREFIX", "unsafe_")
RESERVED_COLNAMES = os.environ.get("CKANEXT__DATAPUSHER_PLUS__RESERVED_COLNAMES", "_id")
PREFER_DMY = tk.asbool(os.environ.get("CKANEXT__DATAPUSHER_PLUS__PREFER_DMY", "False"))
IGNORE_FILE_HASH = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__IGNORE_FILE_HASH", "False")
)

# Indexing settings
AUTO_INDEX_THRESHOLD = tk.asint(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_INDEX_THRESHOLD", "3")
)
AUTO_INDEX_DATES = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_INDEX_DATES", "True")
)
AUTO_UNIQUE_INDEX = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_UNIQUE_INDEX", "True")
)

# Summary statistics settings
SUMMARY_STATS_OPTIONS = os.environ.get("CKANEXT__DATAPUSHER_PLUS__SUMMARY_STATS_OPTIONS")
ADD_SUMMARY_STATS_RESOURCE = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__ADD_SUMMARY_STATS_RESOURCE", "False")
)
SUMMARY_STATS_WITH_PREVIEW = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__SUMMARY_STATS_WITH_PREVIEW", "False")
)
QSV_STATS_STRING_MAX_LENGTH = tk.asint(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__QSV_STATS_STRING_MAX_LENGTH", "32767")
)
# whitelist of case-insensitive dates patterns of column names to use for date inferencing
# date inferencing will only be attempted on columns that match the patterns
# "all" means to scan all columns as date candidates
# date inferencing is an expensive operation, as we try to match on 19 different
# date formats, so we only want to do it on columns that are likely to contain dates
# the default is "date,time,due,open,close,created"
# e.g. "created_date", "open_dt", "issue_closed", "DATE_DUE", "OPEN_DT", "CLOSED_DT", "OPEN_ISSUES"
# will all be scanned as potential date columns. Note that OPEN_ISSUES is likely not a date
# column, but it will still be scanned as a date candidate because it matches the pattern
QSV_DATES_WHITELIST = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__QSV_DATES_WHITELIST", "date,time,due,open,close,created"
)
QSV_FREQ_LIMIT = tk.asint(os.environ.get("CKANEXT__DATAPUSHER_PLUS__QSV_FREQ_LIMIT", "10"))

# Type mapping
TYPE_MAPPING = json.loads(
    os.environ.get(
        "CKANEXT__DATAPUSHER_PLUS__TYPE_MAPPING",
        '{"String": "text", "Integer": "numeric","Float": "numeric","DateTime": "timestamp","Date": "date","NULL": "text"}',
    )
)

# Alias settings
AUTO_ALIAS = tk.asbool(os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_ALIAS", "True"))
AUTO_ALIAS_UNIQUE = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_ALIAS_UNIQUE", "True")
)

# Copy buffer size
COPY_READBUFFER_SIZE = tk.asint(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__COPY_READBUFFER_SIZE", "1048576")
)

# Datastore URLs
DATASTORE_URLS = {
    "datastore_delete": "{ckan_url}/api/action/datastore_delete",
    "resource_update": "{ckan_url}/api/action/resource_update",
}

# Datastore write URL
DATASTORE_WRITE_URL = os.environ.get("CKAN__DATASTORE__WRITE_URL")

# spatial simplification settings
AUTO_SPATIAL_SIMPLIFICATION = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_SPATIAL_SIMPLIFICATION", "True")
)
SPATIAL_SIMPLIFICATION_RELATIVE_TOLERANCE = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__SPATIAL_SIMPLIFICATION_RELATIVE_TOLERANCE", "0.1"
)

# Latitude and longitude column names
# multiple fields can be specified, separated by commas
# matching columns will be from left to right and the jinja2
# variable dpp.LAT_FIELD and dpp.LON_FIELD will be set to the
# value of the first matching column, case-insensitive
LATITUDE_FIELDS = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__LATITUDE_FIELDS",
    "latitude,lat",
)
LONGITUDE_FIELDS = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__LONGITUDE_FIELDS",
    "longitude,lon",
)

# Jinja2 bytecode cache settings
JINJA2_BYTECODE_CACHE_DIR = os.environ.get(
    "CKANEXT__DATAPUSHER_PLUS__JINJA2_BYTECODE_CACHE_DIR", "/tmp/jinja2_bytecode_cache"
)

# if a zip archive is uploaded, and it only contains one file and the file
# is one of the supported formats, automatically unzip the file and pump the
# contents into the datastore. Leave the zip file as the "main" resource.
AUTO_UNZIP_ONE_FILE = tk.asbool(
    os.environ.get("CKANEXT__DATAPUSHER_PLUS__AUTO_UNZIP_ONE_FILE", "True")
)
