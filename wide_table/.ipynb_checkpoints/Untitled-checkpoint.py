{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f48ac9a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h]\n",
      "ipykernel_launcher.py: error: unrecognized arguments: -f /home/notebook/work/.aws-editors-workspace-metadata/runtime/kernel-8525e721-0dee-4a6b-8b78-06e054d9a73f.json\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3445: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# import pyspark\n",
    "import sys\n",
    "import os\n",
    "import argparse\n",
    "import importlib\n",
    "if os.path.exists('python1.zip'):\n",
    "    sys.path.insert(0, 'python1.zip')\n",
    "else:\n",
    "    sys.path.insert(0, './python1')\n",
    "\n",
    "parser = argparse.ArgumentParser()\n",
    "# parser.add_argument('--job', type=str, required=True)\n",
    "# parser.add_argument('--job-args', nargs='*')\n",
    "args = parser.parse_args()\n",
    "\n",
    "# sc = pyspark.SparkContext(appName=args.job_name)\n",
    "job_module = importlib.import_module('python1')\n",
    "print(job_module.aaa())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
