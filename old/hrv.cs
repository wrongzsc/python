    public class HRV
    {
        int mLimit = 20;
        int mSDLimit = 5;
        int mPushCount = 0;
        List<int> mStack = new List<int>();
        List<double> mSDs = new List<double>();

        //push back and pop front
        public void PushData(List<int> data)
        {
            mStack.AddRange(data);

            if (mStack.Count > mLimit)
            {
                mStack.RemoveRange(0, mStack.Count - mLimit);
            }

            mPushCount += data.Count;

            if (mPushCount >= mSDLimit)
            {
                int itertime = mPushCount / mSDLimit;
                List<double> subSD = new List<double>();
                for (int x = 0; x < itertime; x++)
                {
                    List<int> sublist = mStack.GetRange(mStack.Count - (x + 1) * mSDLimit, mSDLimit);
                    subSD.Insert(0, getSD(sublist));
                }

                mSDs.AddRange(subSD);
                mPushCount = 0;
                if (mSDs.Count > mSDLimit)
                {
                    mSDs.RemoveRange(0, mSDs.Count - mSDLimit);
                }
            }
        }

        private double pnnPossession(int pnn)
        {
            double ret = 0;
            int count = 0;
            for (int i = 0; i < mStack.Count - 1; i++)
            {
                if (Math.Abs(mStack[i] - mStack[i] + 1) < pnn)
                {
                    count += 1;
                }

                ret = ((double)count / (double)mStack.Count);
            }
            return ret;
        }

        private double GetMean(List<double> intervals)
        {
            double retval = 0;

            if (intervals.Count > 0)
            {

                for (int i = 0; i < intervals.Count; i++)
                {
                    retval += intervals[i];
                }

                retval /= intervals.Count;
            }

            return retval;
        }

        private double GetMean(List<int> intervals)
        {
            double retval = 0;

            if (intervals.Count > 0)
            {

                for (int i = 0; i < intervals.Count; i++)
                {
                    retval += intervals[i];
                }

                retval /= intervals.Count;
            }

            return retval;
        }

        private double getSD(List<int> intervals)
        {
            double retval = 0;
            double mean = GetMean(intervals);

            for (int i = 0; i < intervals.Count; i++)
            {
                retval += Math.Pow((intervals[i] - mean), 2);
            }

            retval /= intervals.Count;
            retval = Math.Sqrt(retval);

            return retval;
        }

        public string getStatus()
        {
            string ret = "none";
            double pnn50p = pnnPossession(50);
            double pnn30p = pnnPossession(30);

            bool c1 = true;
            bool c2 = true;
            bool c3 = true;

            if (mStack.Count >= 10)
            {
                //pnn possession
                c1 = (pnn50p >= 0.2 || pnn30p >= 0.1);
                //heartbeat rate slower than average
                c3 = (mStack[mStack.Count - 1] >= GetMean(mStack.GetRange(0, mStack.Count - 2)));
            }


            if (mSDs.Count > 4)
            {
                //latest std larger than average std
                c2 = (mSDs[mSDs.Count - 1] >= GetMean(mSDs.GetRange(0, mSDs.Count - 2)));
            }

            if (c1 && c2 && c3)
            {
                ret = "+";
            }
            else if ((c1 && c2) || (c1 && c3) || (c2 && c3))
            {
                ret = "0";
            }
            else
            {
                ret = "-";
            }

            return ret;
        }
    }