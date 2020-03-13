#include <vector>
#include "mine.hpp"

void wait() {
	char c;
	printf("Press Enter to finish\n");
	scanf_s("%c", &c);
}


int main(){
	cout << "n = ? ";
	int n;

	do {
		cin >> n;
		if (n < 5) {
			return 0;
		}

		string a(n, '0'); // "abc63,10,93201920398";
		for (int i1 = 0; i1 < n; i1++) {
			a[i1] = Util::randomInt('0', '9' + 1);
		}

		vector<char> b;
		IOTool::compress(a, b);

		// cout << "a = " << a << endl;

		string c;
		IOTool::decompress(b, c);
		// cout << "c = " << c << endl;

		Util::bin2file(b, mi::detail::TEMP + "z_log.txt");
		vector<char> d;
		Util::file2bin(mi::detail::TEMP + "z_log.txt", d);

		string x;
		IOTool::decompress(d, x);
		// cout << "x = " << x << endl;

		cout << "size " << a.size() << " -> " << b.size()
			<< " <=> " << (double)b.size() / a.size() << endl;
		cout << "a == c ? " << (a == c) << endl;
		cout << "a == x ? " << (a == x) << endl;
	} while (n > 5);

	wait();
}
