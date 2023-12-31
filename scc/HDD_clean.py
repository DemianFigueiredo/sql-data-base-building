{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8f792c3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "90dd81d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>title</th>\n",
       "      <th>release_year</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>PENELOPE</td>\n",
       "      <td>GUINESS</td>\n",
       "      <td>ACADEMY DINOSAUR</td>\n",
       "      <td>2006</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>PENELOPE</td>\n",
       "      <td>GUINESS</td>\n",
       "      <td>ANACONDA CONFESSIONS</td>\n",
       "      <td>2006</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>PENELOPE</td>\n",
       "      <td>GUINESS</td>\n",
       "      <td>ANGELS LIFE</td>\n",
       "      <td>2006</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>PENELOPE</td>\n",
       "      <td>GUINESS</td>\n",
       "      <td>BULWORTH COMMANDMENTS</td>\n",
       "      <td>2006</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>PENELOPE</td>\n",
       "      <td>GUINESS</td>\n",
       "      <td>CHEAPER CLYDE</td>\n",
       "      <td>2006</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  first_name last_name                  title  release_year  category_id\n",
       "0   PENELOPE   GUINESS       ACADEMY DINOSAUR          2006            6\n",
       "1   PENELOPE   GUINESS   ANACONDA CONFESSIONS          2006            2\n",
       "2   PENELOPE   GUINESS            ANGELS LIFE          2006           13\n",
       "3   PENELOPE   GUINESS  BULWORTH COMMANDMENTS          2006           10\n",
       "4   PENELOPE   GUINESS          CHEAPER CLYDE          2006           14"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "old_HDDs = '../data/old_HDD.csv'\n",
    "HDD = pd.read_csv(old_HDDs)\n",
    "pd.set_option('display.max_columns', None)\n",
    "\n",
    "HDD.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "06ce3cef",
   "metadata": {},
   "outputs": [],
   "source": [
    "HDD[[\"first_name\", \"last_name\", \"title\"]] = HDD[[\"first_name\", \"last_name\", \"title\"]].apply(lambda x: x.str.title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dc9962a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>title</th>\n",
       "      <th>release_year</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Academy Dinosaur</td>\n",
       "      <td>2006</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Anaconda Confessions</td>\n",
       "      <td>2006</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Angels Life</td>\n",
       "      <td>2006</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Bulworth Commandments</td>\n",
       "      <td>2006</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Cheaper Clyde</td>\n",
       "      <td>2006</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  first_name last_name                  title  release_year  category_id\n",
       "0   Penelope   Guiness       Academy Dinosaur          2006            6\n",
       "1   Penelope   Guiness   Anaconda Confessions          2006            2\n",
       "2   Penelope   Guiness            Angels Life          2006           13\n",
       "3   Penelope   Guiness  Bulworth Commandments          2006           10\n",
       "4   Penelope   Guiness          Cheaper Clyde          2006           14"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "HDD.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4aac0619",
   "metadata": {},
   "outputs": [],
   "source": [
    "HDD[\"release_year\"] = \"-0001\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e561e25b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>title</th>\n",
       "      <th>release_year</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Academy Dinosaur</td>\n",
       "      <td>-0001</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Anaconda Confessions</td>\n",
       "      <td>-0001</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Angels Life</td>\n",
       "      <td>-0001</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Bulworth Commandments</td>\n",
       "      <td>-0001</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>Cheaper Clyde</td>\n",
       "      <td>-0001</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  first_name last_name                  title release_year  category_id\n",
       "0   Penelope   Guiness       Academy Dinosaur        -0001            6\n",
       "1   Penelope   Guiness   Anaconda Confessions        -0001            2\n",
       "2   Penelope   Guiness            Angels Life        -0001           13\n",
       "3   Penelope   Guiness  Bulworth Commandments        -0001           10\n",
       "4   Penelope   Guiness          Cheaper Clyde        -0001           14"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "HDD.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "de8302a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "column_title = HDD['title']\n",
    "\n",
    "\n",
    "HDD.drop(columns=['title'], inplace=True)\n",
    "\n",
    "\n",
    "HDD.insert(0, 'title', column_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2e4b4571",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>first_name</th>\n",
       "      <th>last_name</th>\n",
       "      <th>release_year</th>\n",
       "      <th>category_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Academy Dinosaur</td>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>-0001</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Anaconda Confessions</td>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>-0001</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Angels Life</td>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>-0001</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bulworth Commandments</td>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>-0001</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Cheaper Clyde</td>\n",
       "      <td>Penelope</td>\n",
       "      <td>Guiness</td>\n",
       "      <td>-0001</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   title first_name last_name release_year  category_id\n",
       "0       Academy Dinosaur   Penelope   Guiness        -0001            6\n",
       "1   Anaconda Confessions   Penelope   Guiness        -0001            2\n",
       "2            Angels Life   Penelope   Guiness        -0001           13\n",
       "3  Bulworth Commandments   Penelope   Guiness        -0001           10\n",
       "4          Cheaper Clyde   Penelope   Guiness        -0001           14"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "HDD.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5ed30bbf",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "HDD.to_csv('hdd_clean.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a592bffc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1000, 5)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "HDD.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af430f8b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73706bb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e80bde0a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e299a27b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af852584",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
