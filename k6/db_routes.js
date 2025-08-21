import { check } from "k6";
import http from "k6/http";

const TEST_DURATION = "5m";
const LOAD_TESTER_DOMAIN = "my-load-tester-domain.com";

export const options = {
  vus: 200,
  duration: TEST_DURATION,
};

export default function () {
  const write_resp = http.post(`https://${LOAD_TESTER_DOMAIN}/write`);

  check(write_resp, { "Status was 200": (r) => r.status == 200 });
}
