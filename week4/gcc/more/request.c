#include <stdio.h>
#include <curl/curl.h>
 
int main(void)
{
	CURL *curl;
	curl = curl_easy_init();
	if(curl) {
	  curl_easy_setopt(curl, CURLOPT_URL, "https://google.com");
	 
	  /* use a GET to fetch this */
	  curl_easy_setopt(curl, CURLOPT_HTTPGET, 1L);
	 
	  /* Perform the request */
	  curl_easy_perform(curl);
	}


}
