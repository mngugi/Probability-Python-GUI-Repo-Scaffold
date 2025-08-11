{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "30315fd8-d0a9-4a9b-bd56-fd81661eaffe",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "attempted relative import with no known parent package",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[2], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtkinter\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mtk\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtkinter\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m messagebox\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mprobability\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m conditional_probability\n\u001b[1;32m      5\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mlaunch_gui\u001b[39m():\n\u001b[1;32m      6\u001b[0m     root \u001b[38;5;241m=\u001b[39m tk\u001b[38;5;241m.\u001b[39mTk()\n",
      "\u001b[0;31mImportError\u001b[0m: attempted relative import with no known parent package"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import messagebox\n",
    "from .probability import conditional_probability\n",
    "\n",
    "def launch_gui():\n",
    "    root = tk.Tk()\n",
    "    root.title(\"Probability Calculator\")\n",
    "\n",
    "    tk.Label(root, text=\"P(A and B):\").grid(row=0, column=0)\n",
    "    entry_a_and_b = tk.Entry(root)\n",
    "    entry_a_and_b.grid(row=0, column=1)\n",
    "\n",
    "    tk.Label(root, text=\"P(A):\").grid(row=1, column=0)\n",
    "    entry_a = tk.Entry(root)\n",
    "    entry_a.grid(row=1, column=1)\n",
    "\n",
    "    def calculate():\n",
    "        try:\n",
    "            p_a_and_b = float(entry_a_and_b.get())\n",
    "            p_a = float(entry_a.get())\n",
    "            result = conditional_probability(p_a_and_b, p_a)\n",
    "            messagebox.showinfo(\"Result\", f\"P(B|A) = {result:.4f}\")\n",
    "        except ValueError:\n",
    "            messagebox.showerror(\"Error\", \"Please enter valid numbers.\")\n",
    "\n",
    "    tk.Button(root, text=\"Calculate\", command=calculate).grid(row=2, column=0, columnspan=2)\n",
    "\n",
    "    root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "557fcdcc-aa6c-48f9-a53f-642de4ec4508",
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
