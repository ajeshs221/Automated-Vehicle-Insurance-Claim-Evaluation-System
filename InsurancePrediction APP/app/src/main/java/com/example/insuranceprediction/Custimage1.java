package com.example.insuranceprediction;

import android.app.Activity;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

public class Custimage1 extends ArrayAdapter<String>  {

	 private Activity context;       //for to get current activity context
	    SharedPreferences sh;


	private String[] vehicleimage;
	private String[] price;


	private String[] statu;
	private String[] vnum;
	private String[] date;


	 public Custimage1(Activity context, String[] vehicleimage, String[] price, String[] statu , String[] date , String[] vnum ) {
	        //constructor of this class to get the values from main_activity_class

		 super(context, R.layout.cust_images1, vehicleimage);
	        this.context = context;
		 this.vehicleimage = vehicleimage;

		 	this.date = date;
		 this.price = price;
		 this.vnum = vnum;

		 this.statu = statu;

	    }

	    @Override
	    public View getView(int position, View convertView, ViewGroup parent) {


			LayoutInflater inflater = context.getLayoutInflater();
			View listViewItem = inflater.inflate(R.layout.cust_images1, null, true);

			ImageView im = (ImageView) listViewItem.findViewById(R.id.imageView1);
			TextView t1=(TextView)listViewItem.findViewById(R.id.textView3);

//			TextView t2=(TextView)listViewItem.findViewById(R.id.textView4);
//			Toast.makeText(getContext(), "kkkk"+statu, Toast.LENGTH_SHORT).show();
			if (statu[position].equals("Rejected")){

				t1.setText("Status : "+statu[position]+"\nDate : "+date[position]+"\nVehicle Number : "+vnum[position]);


			}else if(statu[position].equals("Approved")){

				t1.setText("Claimable % of Bill Amount: "+price[position]+"\nStatus : "+statu[position]+"\nDate : "+date[position]+"\nVehicle Number : "+vnum[position]);
			}else if(statu[position].equals("pending")){

				t1.setText("Status : "+statu[position]+"\nDate : "+date[position]+"\nVehicle Number : "+vnum[position]);
			}

			sh=PreferenceManager.getDefaultSharedPreferences(getContext());

			String pth = "http://"+sh.getString("ip", "")+"/"+vehicleimage[position];
			pth = pth.replace("~", "");


			Log.d("-------------", pth);
			Picasso.with(context)
					.load(pth)
					.placeholder(R.drawable.ic_launcher_background)
					.error(R.drawable.ic_launcher_background).into(im);

			return  listViewItem;
		}

		private TextView setText(String string) {
			// TODO Auto-generated method stub
			return null;
		}
}