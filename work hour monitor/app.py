from flask import Flask, render_template, Request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

