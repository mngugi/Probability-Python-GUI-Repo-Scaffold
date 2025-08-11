{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ba77964d-1a72-424e-9f50-5e0232ee3436",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "attempted relative import with no known parent package",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 4\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# probability_gui/__init__.py\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;66;03m# This makes Python treat the folder as a package.\u001b[39;00m\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mprobability\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mgui\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n\u001b[1;32m      6\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mviz\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n",
      "\u001b[0;31mImportError\u001b[0m: attempted relative import with no known parent package"
     ]
    }
   ],
   "source": [
    "# probability_gui/__init__.py\n",
    "# This makes Python treat the folder as a package.\n",
    "\n",
    "from .probability import *\n",
    "from .gui import *\n",
    "from .viz import *\n",
    "from .main import *\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fd400e9-ca51-4a9b-8f46-e21342d0a724",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
